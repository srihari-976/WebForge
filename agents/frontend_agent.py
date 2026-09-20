from __future__ import annotations

import json
import logging

from agents.base import LocalAgent
from templates.vite_react_saas import render as render_scene_template
from webbuilder.config import CONFIG
from webbuilder.json_utils import parse_json_object
from webbuilder.models import GeneratedProject, JsonDict
from webbuilder.ollama_client import OllamaClient, OllamaUnavailable

logger = logging.getLogger(__name__)

frontend_agent = LocalAgent(
    name="Frontend Developer Agent",
    role="Generates React and Tailwind project files.",
    goal=(
        "Produce complete, responsive, maintainable frontend files that can run in a "
        "local Vite React project."
    ),
    backstory=(
        "You are a senior frontend engineer who favors clear component structure, "
        "stable styling, accessible markup, and templates that reduce fragile blank-page "
        "generation."
    ),
    model=CONFIG.models.frontend,
    system_prompt=(
        "You are an expert React/Tailwind developer. Generate production-quality code.\n"
        "Return a JSON object with a 'files' key mapping relative paths to file contents.\n"
        "Example: {\"files\": {\"src/App.tsx\": \"...\", \"src/styles.css\": \"...\"}}\n"
        "Rules:\n"
        "- Use functional React components with hooks (useState, useEffect)\n"
        "- Use TailwindCSS utility classes for all styling\n"
        "- Import icons from lucide-react\n"
        "- Include real sample data (product arrays, etc.)\n"
        "- Do NOT include placeholder text like 'Lorem ipsum'\n"
        "- Each component should be fully functional with proper props\n"
        "- Use TypeScript (.tsx) for components\n"
        "- The app must compile and run with 'npm run dev'"
    ),
    fallback={"files": {}},
)


CONFIG_FILES = {
    "package.json": lambda wt: json.dumps({
        "name": "generated-app", "private": True, "type": "module",
        "scripts": {"dev": "vite --host 0.0.0.0", "build": "vite build", "preview": "vite preview"},
        "dependencies": {"@vitejs/plugin-react": "latest", "vite": "latest", "typescript": "latest",
                         "react": "latest", "react-dom": "latest", "lucide-react": "latest"},
        "devDependencies": {"tailwindcss": "latest", "@tailwindcss/postcss": "latest",
                            "postcss": "latest", "autoprefixer": "latest"},
    }, indent=2),
    "index.html": lambda wt: f'<!DOCTYPE html>\n<html lang="en">\n<head>\n  <meta charset="UTF-8" />\n  <meta name="viewport" content="width=device-width, initial-scale=1.0" />\n  <title>{wt}</title>\n</head>\n<body>\n  <div id="root"></div>\n  <script type="module" src="/src/main.tsx"></script>\n</body>\n</html>',
    "tsconfig.json": lambda wt: json.dumps({
        "compilerOptions": {"target": "ES2020", "useDefineForClassFields": True, "lib": ["DOM", "DOM.Iterable", "ES2020"],
                            "allowJs": False, "skipLibCheck": True, "esModuleInterop": True, "allowSyntheticDefaultImports": True,
                            "strict": True, "forceConsistentCasingInFileNames": True, "module": "ESNext",
                            "moduleResolution": "Node", "resolveJsonModule": True, "isolatedModules": True,
                            "noEmit": True, "jsx": "react-jsx"},
        "include": ["src"], "references": [],
    }, indent=2),
    "vite.config.ts": lambda wt: "import { defineConfig } from 'vite'\nimport react from '@vitejs/plugin-react'\n\nexport default defineConfig({\n  plugins: [react()],\n})\n",
    "tailwind.config.js": lambda wt: "/** @type {import('tailwindcss').Config} */\nexport default {\n  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],\n  theme: { extend: {} },\n  plugins: [],\n}\n",
    "postcss.config.js": lambda wt: "export default {\n  plugins: {\n    '@tailwindcss/postcss': {},\n  },\n}\n",
    "src/main.tsx": lambda wt: "import React from 'react';\nimport ReactDOM from 'react-dom/client';\nimport App from './App';\nimport './styles.css';\n\nReactDOM.createRoot(document.getElementById('root')!).render(\n  <React.StrictMode>\n    <App />\n  </React.StrictMode>,\n);\n",
    "src/styles.css": lambda wt: '@import "tailwindcss";\n\nbody { margin: 0; }\na { color: inherit; text-decoration: none; }\n',
}


class FrontendDeveloper:
    def generate(self, requirements: JsonDict, plan: JsonDict, client: OllamaClient | None = None) -> GeneratedProject:
        website_type = requirements.get("website_type", "website")
        user_prompt = requirements.get("user_prompt", "")

        # Always generate config files from template
        files = {path: fn(website_type) for path, fn in CONFIG_FILES.items()}

        # Try LLM for app code
        if client is not None:
            try:
                llm_files = self._generate_app_code(requirements, plan, client)
                files.update(llm_files)
                logger.info("LLM generated app code: %d files", len(llm_files))
                return GeneratedProject(
                    files=files,
                    dependencies=["@vitejs/plugin-react", "vite", "typescript", "react", "react-dom", "lucide-react"],
                    dev_dependencies=["tailwindcss", "@tailwindcss/postcss", "postcss", "autoprefixer"],
                    scripts={"dev": "vite --host 0.0.0.0", "build": "vite build", "preview": "vite preview"},
                )
            except Exception as exc:
                logger.warning("LLM generation failed: %s", exc)

        # Fallback: use scene-aware template
        logger.info("Using scene-aware template fallback")
        scene_files = render_scene_template(requirements, plan)
        files.update(scene_files)
        return GeneratedProject(
            files=files,
            dependencies=["@vitejs/plugin-react", "vite", "typescript", "react", "react-dom", "lucide-react"],
            dev_dependencies=["tailwindcss", "@tailwindcss/postcss", "postcss", "autoprefixer"],
            scripts={"dev": "vite --host 0.0.0.0", "build": "vite build", "preview": "vite preview"},
        )

    def _generate_app_code(self, requirements: JsonDict, plan: JsonDict, client: OllamaClient) -> dict[str, str]:
        prompt = self._build_app_prompt(requirements, plan)
        raw = client.generate(CONFIG.models.frontend, prompt=prompt, system=frontend_agent.full_system_prompt)

        logger.debug("LLM raw response (first 500 chars): %s", raw[:500] if raw else "(empty)")

        data = parse_json_object(raw, {"files": {}})
        files = data.get("files", {})

        if not files or not isinstance(files, dict):
            raise ValueError("LLM returned empty files")

        # Filter to only app source files (never overwrite config files)
        CONFIG_PATHS = {"package.json", "index.html", "tsconfig.json", "vite.config.ts",
                        "tailwind.config.js", "postcss.config.js", "src/main.tsx"}
        app_files = {}
        for path, content in files.items():
            if path in CONFIG_PATHS:
                continue  # Never let LLM overwrite config files
            if path.startswith("src/") and path.endswith((".tsx", ".ts", ".css")):
                app_files[path] = content

        if not app_files:
            raise ValueError("LLM did not generate any src/ files")

        return app_files

    @staticmethod
    def _build_app_prompt(requirements: JsonDict, plan: JsonDict) -> str:
        website_type = requirements.get("website_type", "website")
        features = requirements.get("features", [])
        sections = plan.get("sections", ["hero", "features", "contact"])
        primary_color = plan.get("primary_color", "blue")
        theme = requirements.get("theme", "modern")
        user_prompt = requirements.get("user_prompt", "")

        return f"""Generate a React app for: {user_prompt}

Return JSON with "files" key containing src/App.tsx and src/styles.css.

src/App.tsx must be a SINGLE complete React component with:
- useState for interactivity
- TailwindCSS classes for ALL styling
- Import icons from 'lucide-react' like: import {{ Search, Calendar, MapPin }} from 'lucide-react'
- NEVER use @lucide-react/* imports - always use lucide-react directly
- Real sample data (destinations, products, posts)
- All components defined in the same file
- Navigation, hero, content sections, footer

src/styles.css: just '@import "tailwindcss";'

Use double quotes for all strings. No backticks. No template literals.
Return ONLY: {{"files": {{"src/App.tsx": "...", "src/styles.css": "..."}}}}"""


