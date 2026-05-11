from __future__ import annotations

from pathlib import Path

from tools.path_guard import resolve_inside_sandbox


class FileReaderTool:
    def __init__(self, project_dir: str | Path) -> None:
        self.project_path = resolve_inside_sandbox(project_dir)

    def read_text(self, relative_path: str, max_chars: int = 12000) -> str:
        target = (self.project_path / relative_path).resolve()
        if self.project_path not in target.parents and target != self.project_path:
            raise ValueError(f"Requested file escapes project: {relative_path}")
        return target.read_text(encoding="utf-8")[:max_chars]

