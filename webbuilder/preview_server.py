from __future__ import annotations

import logging
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from threading import Thread
from typing import Any

from webbuilder.config import SANDBOX_ROOT

logger = logging.getLogger(__name__)


class PreviewHandler(SimpleHTTPRequestHandler):
    project_path: Path = SANDBOX_ROOT / "generated-app"

    def do_GET(self) -> None:
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status":"ok"}')
            return

        dist = self.project_path / "dist"
        if not dist.exists():
            self.send_error(404, "No built project found. Run a build first.")
            return

        target = dist / self.path.lstrip("/")
        if not target.exists() or not target.is_file():
            index = dist / "index.html"
            if index.exists():
                target = index
            else:
                self.send_error(404, "File not found")
                return

        try:
            content = target.read_bytes()
            content_type = self._guess_type(target.name)
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        except Exception as exc:
            logger.error("Error serving file: %s", exc)
            self.send_error(500, str(exc))

    def _guess_type(self, filename: str) -> str:
        mapping = {
            ".html": "text/html",
            ".css": "text/css",
            ".js": "application/javascript",
            ".json": "application/json",
            ".tsx": "text/javascript",
            ".ts": "text/javascript",
            ".jsx": "text/javascript",
            ".svg": "image/svg+xml",
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".ico": "image/x-icon",
            ".woff": "font/woff",
            ".woff2": "font/woff2",
        }
        from pathlib import PurePath
        ext = PurePath(filename).suffix.lower()
        return mapping.get(ext, "application/octet-stream")

    def log_message(self, format: str, *args: Any) -> None:
        logger.info(format, *args)


def start_preview_server(port: int = 8000, project_dir: str | Path | None = None) -> HTTPServer:
    if project_dir is not None:
        PreviewHandler.project_path = Path(project_dir)

    server = HTTPServer(("0.0.0.0", port), PreviewHandler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    logger.info("Preview server started on http://localhost:%d", port)
    return server
