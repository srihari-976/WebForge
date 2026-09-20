from __future__ import annotations

import logging
from pathlib import Path

from tools.path_guard import resolve_inside_sandbox

logger = logging.getLogger(__name__)

MAX_FILE_SIZE_DEFAULT = 500_000


class FileWriterTool:
    def __init__(self, project_dir: str | Path, max_file_size: int = MAX_FILE_SIZE_DEFAULT) -> None:
        self.project_path = resolve_inside_sandbox(project_dir)
        self.max_file_size = max_file_size

    def write_files(self, files: dict[str, str]) -> list[Path]:
        written: list[Path] = []
        for relative_path, content in files.items():
            if len(content.encode("utf-8")) > self.max_file_size:
                logger.warning("Skipping oversized file %s (%d bytes)", relative_path, len(content.encode("utf-8")))
                continue
            target = (self.project_path / relative_path).resolve()
            if self.project_path not in target.parents and target != self.project_path:
                raise ValueError(f"Generated file escapes project: {relative_path}")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            written.append(target)
            logger.debug("Wrote %s (%d bytes)", relative_path, len(content.encode("utf-8")))
        return written
