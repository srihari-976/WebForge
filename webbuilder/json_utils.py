from __future__ import annotations

import json
import re
from typing import Any


def parse_json_object(text: str, fallback: dict[str, Any]) -> dict[str, Any]:
    text = text.strip()
    if not text:
        return fallback
    try:
        value = json.loads(text)
        return value if isinstance(value, dict) else fallback
    except json.JSONDecodeError:
        pass

    match = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if not match:
        return fallback
    try:
        value = json.loads(match.group(0))
    except json.JSONDecodeError:
        return fallback
    return value if isinstance(value, dict) else fallback

