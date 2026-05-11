from __future__ import annotations

from pathlib import Path

from tools.terminal_tool import TerminalTool
from webbuilder.models import CommandResult


class PackageManagerTool:
    def __init__(self, project_dir: str | Path) -> None:
        self.terminal = TerminalTool(project_dir)

    def install(self, packages: list[str]) -> CommandResult | None:
        if not packages:
            return None
        return self.terminal.run(["npm", "install", *packages], timeout=180)

