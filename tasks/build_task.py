from __future__ import annotations

from typing import Any

from agents.frontend_agent import FrontendDeveloper
from webbuilder.models import GeneratedProject, JsonDict
from webbuilder.ollama_client import OllamaClient


def generate_frontend(requirements: JsonDict, plan: JsonDict, client: OllamaClient | None = None) -> GeneratedProject:
    return FrontendDeveloper().generate(requirements=requirements, plan=plan, client=client)
