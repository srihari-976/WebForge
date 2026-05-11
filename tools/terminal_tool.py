from __future__ import annotations

import subprocess
import shutil
from pathlib import Path

from tools.path_guard import resolve_inside_sandbox
from webbuilder.models import CommandResult


class TerminalTool:
    allowed_commands = {"npm", "node", "npx"}

    def __init__(self, project_dir: str | Path) -> None:
        self.project_path = resolve_inside_sandbox(project_dir)

    def run(self, command: list[str], timeout: int = 120) -> CommandResult:
        if not command or command[0] not in self.allowed_commands:
            raise ValueError(f"Command is not allowlisted: {command}")
        executable = shutil.which(command[0]) or command[0]
        resolved_command = [executable, *command[1:]]
        try:
            completed = subprocess.run(
                resolved_command,
                cwd=self.project_path,
                capture_output=True,
                text=True,
                timeout=timeout,
                shell=False,
            )
        except FileNotFoundError as exc:
            return CommandResult(
                command=command,
                cwd=self.project_path,
                return_code=127,
                stdout="",
                stderr=f"Command not found: {command[0]}. {exc}",
            )
        except subprocess.TimeoutExpired as exc:
            return CommandResult(
                command=command,
                cwd=self.project_path,
                return_code=124,
                stdout=exc.stdout or "",
                stderr=exc.stderr or f"Command timed out after {timeout} seconds.",
            )
        return CommandResult(
            command=command,
            cwd=self.project_path,
            return_code=completed.returncode,
            stdout=completed.stdout,
            stderr=completed.stderr,
        )
