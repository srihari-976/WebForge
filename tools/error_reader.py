from __future__ import annotations

import re

from webbuilder.models import CommandResult

ANSI_PATTERN = re.compile(r"\x1b\[[0-9;]*m")
CONTROL_PATTERN = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")


def sanitize_output(text: str) -> str:
    """Remove ANSI escape codes and control characters from output."""
    text = ANSI_PATTERN.sub("", text)
    text = CONTROL_PATTERN.sub("", text)
    return text


class ErrorLogTool:
    @staticmethod
    def summarize(result: CommandResult, max_chars: int = 4000) -> str:
        output = result.combined_output
        output = sanitize_output(output)
        if len(output) <= max_chars:
            return output
        return output[-max_chars:]
