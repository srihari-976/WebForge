from __future__ import annotations

from pathlib import Path

from tools.path_guard import resolve_inside_sandbox


class FileWriterTool:
    def __init__(self, project_dir: str | Path) -> None:
        self.project_path = resolve_inside_sandbox(project_dir)

    def write_files(self, files: dict[str, str]) -> list[Path]:
        written: list[Path] = []
        for relative_path, content in files.items():
            target = (self.project_path / relative_path).resolve()
            if self.project_path not in target.parents and target != self.project_path:
                raise ValueError(f"Generated file escapes project: {relative_path}")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            written.append(target)
        return written

