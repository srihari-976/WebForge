from __future__ import annotations

from agents.base import LocalAgent
from webbuilder.config import CONFIG


orchestrator_agent = LocalAgent(
    name="Orchestrator Agent",
    role="Controls workflow, delegates tasks, and decides retries.",
    goal=(
        "Convert the user's request into an ordered execution strategy and keep the "
        "build moving from analysis through validation."
    ),
    backstory=(
        "You are the platform lead for a local autonomous web engineering system. "
        "You know which specialist should act next, when to retry, and when to keep "
        "the scope small enough for reliable execution."
    ),
    model=CONFIG.models.orchestrator,
    system_prompt=(
        "You are the orchestration brain for an autonomous web engineering system. "
        "Return compact JSON only. Decide which capabilities are needed."
    ),
    fallback={
        "frontend_needed": True,
        "backend_needed": False,
        "pages": ["home"],
        "retry_on_error": True,
    },
)
