from __future__ import annotations

import json

from agents.debugger_agent import debugger_agent
from webbuilder.models import CommandResult, JsonDict
from webbuilder.ollama_client import OllamaClient


def debug_project(error: CommandResult, scanner_summary: JsonDict, client: OllamaClient) -> JsonDict:
    prompt = (
        "Repair this generated project based on the terminal error.\n"
        f"Command: {' '.join(error.command)}\n"
        f"Exit code: {error.return_code}\n"
        f"Output:\n{error.combined_output[-6000:]}\n"
        f"Project summary:\n{json.dumps(scanner_summary, indent=2)}"
    )
    return debugger_agent.run_json(prompt, client).data

