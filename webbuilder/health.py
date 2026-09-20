from __future__ import annotations

import json
import logging
import re
import urllib.error
import urllib.request
from dataclasses import dataclass

from webbuilder.config import CONFIG

logger = logging.getLogger(__name__)

ANSI_PATTERN = re.compile(r"\x1b\[[0-9;]*m")


@dataclass(frozen=True)
class HealthCheck:
    crewai_installed: bool
    ollama_reachable: bool
    available_models: list[str]
    missing_models: list[str]
    error: str = ""

    @property
    def ok(self) -> bool:
        return self.crewai_installed and self.ollama_reachable and not self.missing_models

    def to_console(self) -> str:
        lines = [
            f"CrewAI installed: {self.crewai_installed}",
            f"Ollama reachable: {self.ollama_reachable}",
            f"Available models: {', '.join(self.available_models) or 'none'}",
            f"Missing required models: {', '.join(self.missing_models) or 'none'}",
        ]
        if self.error:
            error_clean = ANSI_PATTERN.sub("", self.error)
            lines.append(f"Error: {error_clean}")
        lines.append(f"Overall: {'OK' if self.ok else 'NOT READY'}")
        return "\n".join(lines)


def required_models() -> list[str]:
    models = CONFIG.models
    return sorted(
        {
            models.orchestrator,
            models.requirements,
            models.planner,
            models.frontend,
            models.backend,
            models.debugger,
            models.validator,
        }
    )


def check_crewai_installed() -> bool:
    try:
        import crewai  # noqa: F401
    except ImportError:
        return False
    return True


def get_ollama_models(timeout: int = 3) -> list[str]:
    request = urllib.request.Request(f"{CONFIG.ollama_host.rstrip('/')}/api/tags", method="GET")
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = json.loads(response.read().decode("utf-8"))
    return sorted(str(model.get("name", "")) for model in body.get("models", []) if model.get("name"))


def run_health_check() -> HealthCheck:
    crewai_installed = check_crewai_installed()
    try:
        available_models = get_ollama_models()
        ollama_reachable = True
        error = ""
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        available_models = []
        ollama_reachable = False
        error = str(exc)
    missing_models = [model for model in required_models() if model not in available_models]
    return HealthCheck(
        crewai_installed=crewai_installed,
        ollama_reachable=ollama_reachable,
        available_models=available_models,
        missing_models=missing_models,
        error=error,
    )


def ensure_ollama_model_available(model: str) -> None:
    try:
        available_models = get_ollama_models()
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Ollama is not reachable at {CONFIG.ollama_host}: {exc}") from exc
    if model not in available_models:
        raise RuntimeError(f"Ollama model '{model}' is not installed. Run: ollama pull {model}")
