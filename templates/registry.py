from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from typing import Callable

from webbuilder.models import JsonDict

logger = logging.getLogger(__name__)

TemplateRenderer = Callable[[JsonDict, JsonDict], dict[str, str]]

ANSI_PATTERN = re.compile(r"\x1b\[[0-9;]*m")


def sanitize_output(text: str) -> str:
    """Remove ANSI escape codes and control characters from output."""
    text = ANSI_PATTERN.sub("", text)
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", text)
    return text


@dataclass(frozen=True)
class ProjectTemplate:
    name: str
    description: str
    render: TemplateRenderer


class TemplateRegistry:
    def __init__(self) -> None:
        from templates.vite_react_saas import render as vite_react_render
        from templates.nextjs_saas import render as nextjs_render
        from templates.vite_vue import render as vue_render
        from templates.static_html import render as static_render

        self._templates = {
            "vite_react_saas": ProjectTemplate(
                name="vite_react_saas",
                description="Vite React TypeScript SaaS landing page with TailwindCSS.",
                render=vite_react_render,
            ),
            "nextjs_saas": ProjectTemplate(
                name="nextjs_saas",
                description="Next.js App Router SaaS page with TailwindCSS.",
                render=nextjs_render,
            ),
            "vite_vue": ProjectTemplate(
                name="vite_vue",
                description="Vite Vue 3 landing page with TailwindCSS.",
                render=vue_render,
            ),
            "static_html": ProjectTemplate(
                name="static_html",
                description="Pure HTML/CSS static site (no build tools required).",
                render=static_render,
            ),
        }

    def names(self) -> list[str]:
        return sorted(self._templates)

    def get(self, name: str) -> ProjectTemplate:
        return self._templates[name]

    def list_descriptions(self) -> str:
        return "\n".join(
            f"  {name}: {tmpl.description}" for name, tmpl in self._templates.items()
        )
