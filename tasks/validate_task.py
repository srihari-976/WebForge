from __future__ import annotations

from pathlib import Path

from tools.terminal_tool import TerminalTool
from webbuilder.models import CommandResult


def validate_project(project_path: Path, skip_install: bool = False) -> list[CommandResult]:
    terminal = TerminalTool(project_path)
    results: list[CommandResult] = []
    if skip_install:
        return results
    results.append(terminal.run(["npm", "install"], timeout=180))
    if not results[-1].ok:
        return results
    results.append(terminal.run(["npm", "run", "build"], timeout=180))
    return results
