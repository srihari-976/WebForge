from __future__ import annotations

from webbuilder.models import CommandResult


class ErrorLogTool:
    @staticmethod
    def summarize(result: CommandResult, max_chars: int = 4000) -> str:
        output = result.combined_output
        if len(output) <= max_chars:
            return output
        return output[-max_chars:]

