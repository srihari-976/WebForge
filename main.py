from __future__ import annotations

import argparse
import logging
import sys
from datetime import datetime
from pathlib import Path

from agents.base import CrewAIUnavailable
from webbuilder.config import SANDBOX_ROOT
from webbuilder.health import run_health_check
from webbuilder.orchestrator import WebBuilderOrchestrator


def configure_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    fmt = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    logging.basicConfig(level=level, format=fmt, stream=sys.stderr)


def _next_build_dir() -> str:
    """Generate a unique sandbox subfolder like sandbox/build-20260915-112739/."""
    SANDBOX_ROOT.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    folder = f"build-{timestamp}"
    path = SANDBOX_ROOT / folder
    if path.exists():
        i = 2
        while (SANDBOX_ROOT / f"build-{timestamp}-{i}").exists():
            i += 1
        folder = f"build-{timestamp}-{i}"
    return f"sandbox/{folder}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="WebForge - Autonomous Webpage Builder")
    parser.add_argument("prompt", nargs="?", help="Website or app request to build")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check CrewAI, Ollama, and required local models without building",
    )
    parser.add_argument(
        "--project-dir",
        default=None,
        help="Sandbox-relative output directory (default: auto-generated unique folder)",
    )
    parser.add_argument(
        "--skip-install",
        action="store_true",
        help="Write files but skip npm install/build validation",
    )
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Start a local preview server after building",
    )
    parser.add_argument(
        "--preview-port",
        type=int,
        default=8000,
        help="Port for the preview server (default: 8000)",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose debug logging",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    configure_logging(verbose=args.verbose)

    if args.check:
        print(run_health_check().to_console())
        return

    if not args.prompt:
        raise SystemExit("Prompt is required unless --check is used.")

    project_dir = args.project_dir or _next_build_dir()
    print(f"Building to: {SANDBOX_ROOT / Path(project_dir).name}")

    orchestrator = WebBuilderOrchestrator()
    try:
        result = orchestrator.build(
            user_prompt=args.prompt,
            project_dir=project_dir,
            skip_install=args.skip_install,
        )
    except CrewAIUnavailable as exc:
        raise SystemExit(f"CrewAI run failed: {exc}") from exc

    print(result.to_console())

    if args.preview:
        from webbuilder.preview_server import start_preview_server
        print(f"Starting preview server on http://localhost:{args.preview_port}")
        server = start_preview_server(port=args.preview_port, project_dir=project_dir)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nPreview server stopped.")


if __name__ == "__main__":
    main()
