from __future__ import annotations

import json

from agents.base import LocalAgent
from templates.registry import TemplateRegistry
from webbuilder.config import CONFIG
from webbuilder.models import GeneratedProject, JsonDict


frontend_agent = LocalAgent(
    name="Frontend Developer Agent",
    role="Generates React and Tailwind project files.",
    goal=(
        "Produce complete, responsive, maintainable frontend files that can run in a "
        "local Vite React project."
    ),
    backstory=(
        "You are a senior frontend engineer who favors clear component structure, "
        "stable styling, accessible markup, and templates that reduce fragile blank-page "
        "generation."
    ),
    model=CONFIG.models.frontend,
    system_prompt=(
        "Generate production-quality React/Tailwind code as JSON only. "
        "The JSON must contain a files object mapping relative paths to file contents."
    ),
    fallback={"files": {}},
)


class FrontendDeveloper:
    def __init__(self, registry: TemplateRegistry | None = None) -> None:
        self.registry = registry or TemplateRegistry()

    def generate(self, requirements: JsonDict, plan: JsonDict) -> GeneratedProject:
        template = self.registry.get("vite_react_saas")
        files = template.render(requirements=requirements, plan=plan)
        return GeneratedProject(
            files=files,
            dependencies=["@vitejs/plugin-react", "vite", "typescript", "react", "react-dom", "lucide-react"],
            dev_dependencies=[],
            scripts={"dev": "vite --host 0.0.0.0", "build": "vite build", "preview": "vite preview"},
        )

    @staticmethod
    def prompt_for_generation(requirements: JsonDict, plan: JsonDict) -> str:
        return (
            "Generate a Vite React Tailwind project.\n"
            f"Requirements:\n{json.dumps(requirements, indent=2)}\n"
            f"Plan:\n{json.dumps(plan, indent=2)}\n"
            "Return JSON only: {\"files\": {\"path\": \"content\"}}"
        )
