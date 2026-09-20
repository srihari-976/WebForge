from __future__ import annotations

import json
import logging
import re
from typing import Any

logger = logging.getLogger(__name__)


def parse_json_object(text: str, fallback: dict[str, Any]) -> dict[str, Any]:
    text = text.strip()
    if not text:
        return fallback

    # Strip markdown code fences
    text = re.sub(r"```(?:json)?\s*", "", text)
    text = re.sub(r"```\s*$", "", text)
    text = text.strip()

    # Replace multi-line backtick strings with double-quoted strings
    # Handle `...` patterns spanning multiple lines
    def replace_backticks(m):
        content = m.group(1)
        # Escape double quotes and backslashes for JSON
        content = content.replace('\\', '\\\\').replace('"', '\\"')
        # Replace newlines with \n for JSON
        content = content.replace('\n', '\\n').replace('\r', '')
        return '"' + content + '"'

    text = re.sub(r'`([^`]*)`', replace_backticks, text, flags=re.DOTALL)

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

