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
        npm_packages = [p for p in packages if not p.startswith("pip:")]
        pip_packages = [p[4:] for p in packages if p.startswith("pip:")]

        result: CommandResult | None = None
        if npm_packages:
            result = self.terminal.run(["npm", "install", *npm_packages], timeout=180)
        if pip_packages:
            pip_result = self.terminal.run(["pip", "install", *pip_packages], timeout=180)
            if result is None:
                result = pip_result
            elif not pip_result.ok:
                result = pip_result
        return result
