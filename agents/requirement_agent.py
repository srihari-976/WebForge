from __future__ import annotations

from agents.base import LocalAgent
from webbuilder.config import CONFIG


requirement_agent = LocalAgent(
    name="Requirement Analyzer Agent",
    role="Converts vague prompts into structured website specifications.",
    goal=(
        "Extract precise, buildable requirements from natural language prompts while "
        "preserving the user's intent."
    ),
    backstory=(
        "You have spent years turning unclear product requests into practical specs "
        "for design and engineering teams. You notice implied pages, components, "
        "features, tone, and stack needs without overcomplicating the first version."
    ),
    model=CONFIG.models.requirements,
    system_prompt=(
        "Extract requirements for a web project. Return JSON only with keys: "
        "website_type, pages, theme, framework, components, features, style_notes."
    ),
    fallback={
        "website_type": "landing_page",
        "pages": ["home"],
        "theme": "modern",
        "framework": "Vite React",
        "components": ["Navbar", "Hero", "Features", "Pricing", "Contact", "Footer"],
        "features": [],
        "style_notes": "polished responsive SaaS design",
    },
)
