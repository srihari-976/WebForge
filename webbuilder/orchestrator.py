from __future__ import annotations

from agents.orchestrator import orchestrator_agent
from tasks.analyze_task import analyze_user_prompt
from tasks.build_task import generate_frontend
from tasks.debug_task import debug_project
from tasks.plan_task import create_project_plan
from tasks.validate_task import validate_project
from tools.file_writer import FileWriterTool
from tools.package_manager import PackageManagerTool
from tools.project_scanner import ProjectScannerTool
from tools.path_guard import resolve_inside_sandbox
from webbuilder.config import CONFIG
from webbuilder.models import BuildResult, CommandResult
from webbuilder.ollama_client import OllamaClient


class WebBuilderOrchestrator:
    def __init__(self, client: OllamaClient | None = None) -> None:
        self.client = client or OllamaClient()

    def build(self, user_prompt: str, project_dir: str, skip_install: bool = False) -> BuildResult:
        project_path = resolve_inside_sandbox(project_dir)
        orchestration = orchestrator_agent.run_json(
            f"Decide workflow needs for this request: {user_prompt}",
            self.client,
        ).data
        requirements = analyze_user_prompt(user_prompt, self.client)
        requirements.setdefault("pages", orchestration.get("pages", ["home"]))
        plan = create_project_plan(requirements, self.client)

        generated = generate_frontend(requirements, plan)
        writer = FileWriterTool(project_dir)
        writer.write_files(generated.files)

        validation: list[CommandResult] = validate_project(project_path, skip_install=skip_install)
        repaired = False

        for _ in range(CONFIG.retry_limit):
            failed = next((result for result in validation if not result.ok), None)
            if failed is None:
                break
            scanner_summary = ProjectScannerTool(project_path).scan()
            repair = debug_project(failed, scanner_summary, self.client)
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

        success = True if skip_install else bool(validation) and all(result.ok for result in validation)

        return BuildResult(
            project_path=project_path,
            requirements=requirements,
            plan=plan,
            validation=validation,
            repaired=repaired,
            success=success,
        )
