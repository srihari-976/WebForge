from __future__ import annotations

from pathlib import Path

from webbuilder.config import SANDBOX_ROOT


def resolve_inside_sandbox(path: str | Path) -> Path:
    SANDBOX_ROOT.mkdir(parents=True, exist_ok=True)
    raw = Path(path)
    if raw.is_absolute():
        candidate = raw
    elif raw.parts and raw.parts[0] == SANDBOX_ROOT.name:
        candidate = SANDBOX_ROOT.parent / raw
    else:
        candidate = SANDBOX_ROOT / raw
    resolved = candidate.resolve()
    sandbox = SANDBOX_ROOT.resolve()
    if resolved != sandbox and sandbox not in resolved.parents:
        raise ValueError(f"Path escapes sandbox: {path}")
    return resolved
