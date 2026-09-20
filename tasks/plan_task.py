from __future__ import annotations

import json

from agents.uiux_planner import uiux_planner_agent
from webbuilder.models import JsonDict
from webbuilder.normalizers import normalize_plan
from webbuilder.ollama_client import OllamaClient


def create_project_plan(requirements: JsonDict, client: OllamaClient, prompt: str = "") -> JsonDict:
    task_prompt = (
        "Create an implementation plan for these requirements.\n"
        f"{json.dumps(requirements, indent=2)}\n\n"
        "Return JSON with: layout, primary_color, sections, component_tree, responsive_rules.\n"
        "Choose sections that match the website type."
    )
    return normalize_plan(uiux_planner_agent.run_json(task_prompt, client).data, prompt=prompt)
