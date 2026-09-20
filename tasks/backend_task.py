from __future__ import annotations

import json

from agents.backend_agent import backend_agent
from webbuilder.models import GeneratedProject, JsonDict
from webbuilder.ollama_client import OllamaClient


def generate_backend(requirements: JsonDict, client: OllamaClient) -> GeneratedProject | None:
    if not requirements.get("features"):
        return None

    needs_backend = any(
        keyword in json.dumps(requirements).lower()
        for keyword in ["api", "database", "auth", "login", "signup", "crud", "backend", "server"]
    )
    if not needs_backend:
        return None

    prompt = (
        "Determine if this project needs a backend. If yes, generate FastAPI backend files.\n"
        f"Requirements:\n{json.dumps(requirements, indent=2)}\n\n"
        "Return JSON with: backend_needed (bool), files (dict of relative_path -> content)."
    )
    result = backend_agent.run_json(prompt, client)
    data = result.data

    if not data.get("backend_needed") or not data.get("files"):
        return None

    files = data["files"]
    if not isinstance(files, dict):
        return None

    return GeneratedProject(
        files=files,
        dependencies=["fastapi", "uvicorn"],
        dev_dependencies=[],
        scripts={"backend": "uvicorn api.main:app --reload"},
    )
