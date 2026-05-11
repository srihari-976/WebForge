from __future__ import annotations

import argparse

from agents.base import CrewAIUnavailable
from webbuilder.health import run_health_check
from webbuilder.orchestrator import WebBuilderOrchestrator


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Autonomous Webpage Builder")
    parser.add_argument("prompt", nargs="?", help="Website or app request to build")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check CrewAI, Ollama, and required local models without building",
    )
    parser.add_argument(
        "--project-dir",
        default="sandbox/generated-app",
        help="Sandbox-relative output directory for the generated project",
    )
    parser.add_argument(
        "--skip-install",
        action="store_true",
        help="Write files but skip npm install/build validation",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.check:
        print(run_health_check().to_console())
        return
    if not args.prompt:
        raise SystemExit("Prompt is required unless --check is used.")
    orchestrator = WebBuilderOrchestrator()
    try:
        result = orchestrator.build(
            user_prompt=args.prompt,
            project_dir=args.project_dir,
            skip_install=args.skip_install,
        )
    except CrewAIUnavailable as exc:
        raise SystemExit(f"CrewAI run failed: {exc}") from exc
    print(result.to_console())


if __name__ == "__main__":
    main()
