from __future__ import annotations

import json

from agents.uiux_planner import uiux_planner_agent
from webbuilder.models import JsonDict
from webbuilder.normalizers import normalize_plan
from webbuilder.ollama_client import OllamaClient


def create_project_plan(requirements: JsonDict, client: OllamaClient) -> JsonDict:
    task_prompt = (
        "Create an implementation plan for these requirements.\n"
        f"{json.dumps(requirements, indent=2)}"
    )
    return normalize_plan(uiux_planner_agent.run_json(task_prompt, client).data)
