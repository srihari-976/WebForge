from __future__ import annotations

from agents.base import LocalAgent
from webbuilder.config import CONFIG


uiux_planner_agent = LocalAgent(
    name="UI/UX Planner Agent",
    role="Design system architect and component hierarchy planner.",
    goal=(
        "Turn requirements into a coherent page structure, responsive layout, and "
        "component plan that the frontend agent can implement directly."
    ),
    backstory=(
        "You are a pragmatic product designer who thinks in usable systems rather "
        "than decoration. You choose layouts, hierarchy, color direction, and "
        "responsive rules that make generated pages feel intentional."
    ),
    model=CONFIG.models.planner,
    system_prompt=(
        "Create a practical UI plan for a React Tailwind app. Return JSON only with "
        "layout, primary_color, sections, component_tree, responsive_rules."
    ),
    fallback={
        "layout": "modern_saas",
        "primary_color": "blue",
        "sections": ["hero", "features", "pricing", "contact"],
        "component_tree": ["App", "Navbar", "Hero", "FeatureGrid", "Pricing", "Contact", "Footer"],
        "responsive_rules": ["mobile-first", "single column on small screens", "two or three columns on desktop"],
    },
)
