from __future__ import annotations

from agents.requirement_agent import requirement_agent
from webbuilder.models import JsonDict
from webbuilder.normalizers import normalize_requirements
from webbuilder.ollama_client import OllamaClient


def analyze_user_prompt(prompt: str, client: OllamaClient) -> JsonDict:
    task_prompt = (
        "Analyze this website/app request and produce structured requirements.\n"
        f"User request: {prompt}\n\n"
        "Return JSON with keys: website_type, pages, theme, framework, components, features, style_notes.\n"
        "Make features specific to the user's request, not generic."
    )
    return normalize_requirements(requirement_agent.run_json(task_prompt, client).data, prompt=prompt)
