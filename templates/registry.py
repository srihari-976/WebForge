from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from webbuilder.models import JsonDict


TemplateRenderer = Callable[[JsonDict, JsonDict], dict[str, str]]


@dataclass(frozen=True)
class ProjectTemplate:
    name: str
    description: str
    render: TemplateRenderer


class TemplateRegistry:
    def __init__(self) -> None:
        from templates.vite_react_saas import render

        self._templates = {
            "vite_react_saas": ProjectTemplate(
                name="vite_react_saas",
                description="Vite React TypeScript SaaS landing page with Tailwind-style CSS.",
                render=render,
            )
        }

    def names(self) -> list[str]:
        return sorted(self._templates)

    def get(self, name: str) -> ProjectTemplate:
        return self._templates[name]

