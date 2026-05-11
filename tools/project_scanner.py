from __future__ import annotations

import json
from pathlib import Path

from tools.path_guard import resolve_inside_sandbox
from webbuilder.models import JsonDict


class ProjectScannerTool:
    ignored_dirs = {"node_modules", "dist", ".next", ".git"}

    def __init__(self, project_dir: str | Path) -> None:
        self.project_path = resolve_inside_sandbox(project_dir)

    def scan(self) -> JsonDict:
        files: list[str] = []
        package: JsonDict = {}
        for path in self.project_path.rglob("*"):
            if any(part in self.ignored_dirs for part in path.parts):
                continue
            if path.is_file():
                files.append(path.relative_to(self.project_path).as_posix())
        package_path = self.project_path / "package.json"
        if package_path.exists():
            package = json.loads(package_path.read_text(encoding="utf-8"))
        return {"root": str(self.project_path), "files": files[:200], "package": package}

