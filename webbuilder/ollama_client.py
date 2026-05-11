from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any

from webbuilder.config import CONFIG


class OllamaUnavailable(RuntimeError):
    """Raised when the local Ollama service is not reachable."""


class OllamaClient:
    def __init__(self, host: str = CONFIG.ollama_host, timeout: int = CONFIG.ollama_timeout) -> None:
        self.host = host.rstrip("/")
        self.timeout = timeout

    def generate(self, model: str, prompt: str, system: str = "") -> str:
        payload: dict[str, Any] = {
            "model": model,
            "prompt": prompt,
            "system": system,
            "stream": False,
            "options": {"temperature": 0.2},
        }
        data = json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            f"{self.host}/api/generate",
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                body = json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, TimeoutError) as exc:
            raise OllamaUnavailable(str(exc)) from exc
        return str(body.get("response", "")).strip()
