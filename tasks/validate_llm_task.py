from __future__ import annotations

import json

from agents.validator_agent import validator_agent
from webbuilder.models import JsonDict, CommandResult
from webbuilder.ollama_client import OllamaClient
from tools.project_scanner import ProjectScannerTool
from pathlib import Path


def validate_with_llm(
    project_path: Path,
    validation_results: list[CommandResult],
    client: OllamaClient,
) -> JsonDict:
    scanner = ProjectScannerTool(project_path)
    summary = scanner.scan()

    failed = [r for r in validation_results if not r.ok]
    error_details = "\n".join(
        f"Command: {' '.join(r.command)}\nExit code: {r.return_code}\nOutput:\n{r.combined_output[-2000:]}"
        for r in failed
    ) if failed else "No failures"

    prompt = (
        "Validate this generated project. Check for:\n"
        "- Missing files or imports\n"
        "- Dependency issues\n"
        "- Structural problems\n\n"
        f"Project structure:\n{json.dumps(summary, indent=2)}\n\n"
        f"Validation results:\n{error_details}\n\n"
        "Return JSON with: valid (bool), issues (list of strings), suggestions (list of strings)."
    )
    return validator_agent.run_json(prompt, client).data
