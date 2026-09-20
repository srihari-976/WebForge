from __future__ import annotations

import json
import logging
import time
import urllib.error
import urllib.request
from typing import Any

from webbuilder.config import CONFIG

logger = logging.getLogger(__name__)


class OllamaUnavailable(RuntimeError):
    """Raised when the local Ollama service is not reachable."""


class OllamaClient:
    def __init__(
        self,
        host: str = CONFIG.ollama_host,
        timeout: int = CONFIG.ollama_timeout,
        max_retries: int = 3,
        backoff_base: float = 1.0,
    ) -> None:
        self.host = host.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.backoff_base = backoff_base

    def generate(self, model: str, prompt: str, system: str = "") -> str:
        payload: dict[str, Any] = {
            "model": model,
            "prompt": prompt,
            "system": system,
            "stream": False,
            "options": {"temperature": 0.2},
        }
        data = json.dumps(payload).encode("utf-8")

        last_exc: Exception | None = None
        for attempt in range(self.max_retries):
            request = urllib.request.Request(
                f"{self.host}/api/generate",
                data=data,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    body = json.loads(response.read().decode("utf-8"))
                return str(body.get("response", "")).strip()
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
                last_exc = exc
                if attempt < self.max_retries - 1:
                    delay = self.backoff_base * (2 ** attempt)
                    logger.warning(
                        "Ollama request failed (attempt %d/%d), retrying in %.1fs: %s",
                        attempt + 1,
                        self.max_retries,
                        delay,
                        exc,
                    )
                    time.sleep(delay)

        raise OllamaUnavailable(f"Ollama unavailable after {self.max_retries} attempts: {last_exc}")
