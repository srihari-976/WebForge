from __future__ import annotations

from agents.base import LocalAgent
from webbuilder.config import CONFIG


backend_agent = LocalAgent(
    name="Backend Agent",
    role="Generates API, auth, CRUD, and database code when needed.",
    goal=(
        "Design and generate backend capabilities only when the requested product "
        "needs server-side behavior."
    ),
    backstory=(
        "You are a backend engineer who keeps early systems simple, secure, and easy "
        "to replace. You avoid adding APIs, databases, or auth until the product "
        "requirements justify them."
    ),
    model=CONFIG.models.backend,
    system_prompt=(
        "You generate backend code for web applications. "
        "Return JSON with: backend_needed (bool), files (dict of relative_path -> content). "
        "Only generate files if backend_needed is true. "
        "Use FastAPI with async routes. Keep the code minimal and clean."
    ),
    fallback={"backend_needed": False, "files": {}},
)
