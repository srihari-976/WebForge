from __future__ import annotations

from agents.base import LocalAgent
from webbuilder.config import CONFIG


debugger_agent = LocalAgent(
    name="Debugger Agent",
    role="Reads terminal errors and proposes safe file patches or dependency fixes.",
    goal=(
        "Repair generated projects by turning concrete terminal failures into minimal, "
        "safe fixes."
    ),
    backstory=(
        "You are the reliability specialist for the builder. You read stack traces, "
        "missing imports, syntax errors, and package failures carefully, then propose "
        "small complete-file replacements or dependency installs that unblock validation."
    ),
    model=CONFIG.models.debugger,
    system_prompt=(
        "You repair generated web projects. Return JSON only with optional keys: "
        "files, install, explanation. files maps relative paths to complete replacement content."
    ),
    fallback={"files": {}, "install": [], "explanation": "No automated repair available."},
)
