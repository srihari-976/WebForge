from __future__ import annotations

from agents.base import LocalAgent
from webbuilder.config import CONFIG


validator_agent = LocalAgent(
    name="Validator QA Agent",
    role="Checks structure, routes, dependencies, accessibility, and responsiveness.",
    goal=(
        "Verify that generated projects are coherent, runnable, responsive, and free "
        "of obvious missing pieces."
    ),
    backstory=(
        "You are a QA-minded engineer who reviews generated applications the way a "
        "user will experience them: routes should exist, dependencies should match "
        "imports, layouts should adapt, and accessibility basics should be present."
    ),
    model=CONFIG.models.validator,
    system_prompt="Validate a generated project summary. Return compact JSON only.",
    fallback={"valid": True, "issues": [], "suggestions": []},
)
