from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


JsonDict = dict[str, Any]


@dataclass
class AgentOutput:
    raw: str
    data: JsonDict


@dataclass
class GeneratedProject:
    files: dict[str, str]
    dependencies: list[str] = field(default_factory=list)
    dev_dependencies: list[str] = field(default_factory=list)
    scripts: dict[str, str] = field(default_factory=dict)


@dataclass
class CommandResult:
    command: list[str]
    cwd: Path
    return_code: int
    stdout: str
    stderr: str

    @property
    def ok(self) -> bool:
        return self.return_code == 0

    @property
    def combined_output(self) -> str:
        return "\n".join(part for part in [self.stdout, self.stderr] if part).strip()


@dataclass
class BuildResult:
    project_path: Path
    requirements: JsonDict
    plan: JsonDict
    validation: list[CommandResult]
    repaired: bool
    success: bool

    def to_console(self) -> str:
        status = "SUCCESS" if self.success else "FAILED"
        lines = [
            f"Build status: {status}",
            f"Project path: {self.project_path}",
            f"Website type: {self.requirements.get('website_type', 'unknown')}",
            f"Pages: {', '.join(self.requirements.get('pages', [])) or 'home'}",
            f"Repaired during run: {self.repaired}",
        ]
        if self.validation:
            lines.append("Validation:")
            for result in self.validation:
                command = " ".join(result.command)
                lines.append(f"  - {command}: exit {result.return_code}")
        return "\n".join(lines)

