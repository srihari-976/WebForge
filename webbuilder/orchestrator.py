from __future__ import annotations

import logging
from pathlib import Path

from agents.orchestrator import orchestrator_agent
from tasks.analyze_task import analyze_user_prompt
from tasks.build_task import generate_frontend
from tasks.backend_task import generate_backend
from tasks.debug_task import debug_project
from tasks.plan_task import create_project_plan
from tasks.validate_task import validate_project
from tasks.validate_llm_task import validate_with_llm
from tools.file_writer import FileWriterTool
from tools.package_manager import PackageManagerTool
from tools.project_scanner import ProjectScannerTool
from tools.path_guard import resolve_inside_sandbox
from webbuilder.config import CONFIG
from webbuilder.models import BuildResult, CommandResult, JsonDict
from webbuilder.ollama_client import OllamaClient

logger = logging.getLogger(__name__)

ESSENTIAL_FILES = {"package.json", "index.html", "src/App.tsx", "vite.config.ts"}


def _check_essential_files(project_path: Path) -> list[str]:
    missing: list[str] = []
    for rel in ESSENTIAL_FILES:
        candidate = project_path / rel
        if not candidate.exists() or candidate.stat().st_size == 0:
            missing.append(rel)
    return missing


class WebBuilderOrchestrator:
    def __init__(self, client: OllamaClient | None = None) -> None:
        self.client = client or OllamaClient()

    def build(self, user_prompt: str, project_dir: str, skip_install: bool = False) -> BuildResult:
        project_path = resolve_inside_sandbox(project_dir)
        logger.info("Starting build for project: %s", project_path)

        orchestration = orchestrator_agent.run_json(
            f"Decide workflow needs for this request: {user_prompt}",
            self.client,
        ).data
        logger.debug("Orchestration result: %s", orchestration)

        requirements = analyze_user_prompt(user_prompt, self.client)
        requirements.setdefault("pages", orchestration.get("pages", ["home"]))
        logger.info("Requirements analyzed: %s", requirements.get("website_type", "unknown"))

        plan = create_project_plan(requirements, self.client, prompt=user_prompt)
        logger.info("Project plan created: %s", plan.get("layout", "unknown"))

        generated = generate_frontend(requirements, plan, client=self.client)

        backend = generate_backend(requirements, self.client)
        if backend is not None:
            generated.files.update(backend.files)
            generated.dependencies.extend(backend.dependencies)
            generated.dev_dependencies.extend(backend.dev_dependencies)
            generated.scripts.update(backend.scripts)
            logger.info("Backend generation completed")

        writer = FileWriterTool(project_dir)
        written_files = writer.write_files(generated.files)
        logger.info("Wrote %d files to %s", len(written_files), project_path)

        if skip_install:
            missing = _check_essential_files(project_path)
            if missing:
                logger.warning("Essential files missing: %s", missing)
                success = False
            else:
                logger.info("File integrity check passed (skip_install mode)")
                success = True
            return BuildResult(
                project_path=project_path,
                requirements=requirements,
                plan=plan,
                validation=[],
                repaired=False,
                success=success,
            )

        validation: list[CommandResult] = validate_project(project_path, skip_install=False)
        repaired = False

        for attempt in range(CONFIG.retry_limit):
            failed = next((result for result in validation if not result.ok), None)
            if failed is None:
                break
            logger.warning("Build failed (attempt %d/%d), running debugger", attempt + 1, CONFIG.retry_limit)
            scanner_summary = ProjectScannerTool(project_path).scan()
            repair = debug_project(failed, scanner_summary, self.client)
            logger.info("Debugger repair: %s", repair.get("explanation", "no explanation"))

            install_result = PackageManagerTool(project_path).install(list(repair.get("install", [])))
            if install_result is not None:
                validation.append(install_result)
                if not install_result.ok:
                    break

            files = repair.get("files", {})
            if isinstance(files, dict) and files:
                writer.write_files({str(path): str(content) for path, content in files.items()})
                repaired = True
            else:
                break

            validation = validate_project(project_path, skip_install=True)

        llm_validation = validate_with_llm(project_path, validation, self.client)
        if not llm_validation.get("valid", True):
            logger.warning("LLM validation found issues: %s", llm_validation.get("issues", []))

        success = bool(validation) and all(result.ok for result in validation)
        logger.info("Build finished: success=%s", success)

        return BuildResult(
            project_path=project_path,
            requirements=requirements,
            plan=plan,
            validation=validation,
            repaired=repaired,
            success=success,
        )
