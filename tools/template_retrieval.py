from __future__ import annotations

from templates.registry import TemplateRegistry


class TemplateRetrievalTool:
    def __init__(self) -> None:
        self.registry = TemplateRegistry()

    def list_templates(self) -> list[str]:
        return self.registry.names()

    def get_template(self, name: str):
        return self.registry.get(name)

