from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SANDBOX_ROOT = REPO_ROOT / "sandbox"
TEMPLATE_ROOT = REPO_ROOT / "templates"


@dataclass(frozen=True)
class ModelConfig:
    orchestrator: str = os.getenv("WEBBUILDER_ORCHESTRATOR_MODEL", "qwen2.5:1.5b")
    requirements: str = os.getenv("WEBBUILDER_REQUIREMENTS_MODEL", "qwen2.5:3b")
    planner: str = os.getenv("WEBBUILDER_PLANNER_MODEL", "qwen2.5-coder:3b")
    frontend: str = os.getenv("WEBBUILDER_FRONTEND_MODEL", "qwen2.5-coder:3b")
    backend: str = os.getenv("WEBBUILDER_BACKEND_MODEL", "qwen2.5-coder:3b")
    debugger: str = os.getenv("WEBBUILDER_DEBUGGER_MODEL", "qwen2.5-coder:3b")
    validator: str = os.getenv("WEBBUILDER_VALIDATOR_MODEL", "qwen2.5-coder:3b")


@dataclass(frozen=True)
class AppConfig:
    ollama_host: str = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    ollama_timeout: int = int(os.getenv("OLLAMA_TIMEOUT", "180"))
    retry_limit: int = int(os.getenv("WEBBUILDER_RETRY_LIMIT", "2"))
    use_crewai: bool = os.getenv("WEBBUILDER_USE_CREWAI", "true").lower() == "true"
    require_crewai: bool = os.getenv("WEBBUILDER_REQUIRE_CREWAI", "false").lower() == "true"
    max_file_size: int = int(os.getenv("WEBBUILDER_MAX_FILE_SIZE", "500000"))
    models: ModelConfig = ModelConfig()


CONFIG = AppConfig()
