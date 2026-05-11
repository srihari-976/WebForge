from __future__ import annotations

from agents.frontend_agent import FrontendDeveloper
from webbuilder.models import GeneratedProject, JsonDict


def generate_frontend(requirements: JsonDict, plan: JsonDict) -> GeneratedProject:
    return FrontendDeveloper().generate(requirements=requirements, plan=plan)

