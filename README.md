# WebForge

AI full-stack autonomous web engineering scaffold using CrewAI, local Ollama models, template retrieval, sandboxed file writing, terminal execution, validation, and an automated debug loop.

## What This MVP Does

- Turns a user prompt into structured requirements.
- Plans a React/Tailwind webpage architecture.
- Retrieves a high-quality starter template.
- Generates project files into `sandbox/generated-app`.
- Runs `npm install` and `npm run build` for validation when Node tooling is available.
- Captures terminal errors and asks a debugger agent for repair patches.
- Retries validation up to a configurable limit.
- Validates generated project structure with an LLM-based validator agent.
- Generates backend code (FastAPI) when the prompt requires API/database/auth.
- Supports multiple templates: Vite React, Next.js, Vue, and static HTML.

## Project Layout

```text
agents/       Agent definitions and prompts
tasks/        Workflow task wrappers
tools/        Sandboxed file, terminal, scan, package, and error tools
templates/    Reusable project templates (4 available)
sandbox/      Generated applications live here
webbuilder/   Core orchestration runtime
main.py       CLI entry point
```

## Requirements

- Python 3.10+
- Ollama running locally
- CrewAI installed from `requirements.txt`
- Recommended local models:
  - `qwen2.5:1.5b` (orchestration)
  - `qwen2.5:3b` (requirements analysis)
  - `qwen2.5-coder:3b` (frontend, backend, debugging, planning)
  - Optional stronger debugger: `qwen2.5-coder:7b`
- Node.js and npm for generated frontend validation

## Quick Start

```bash
pip install -r requirements.txt
python main.py "Build a modern AI SaaS landing page with pricing and contact sections"
```

The generated app is written to:

```text
sandbox/generated-app
```

## Configuration

Copy `.env.example` to `.env` and adjust values, or set environment variables:

```bash
export OLLAMA_HOST="http://localhost:11434"
export OLLAMA_TIMEOUT="180"
export WEBBUILDER_RETRY_LIMIT="2"
export WEBBUILDER_DEBUGGER_MODEL="qwen2.5-coder:7b"
```

CrewAI is enabled by default. For local template smoke tests without CrewAI/Ollama:

```bash
export WEBBUILDER_USE_CREWAI=false
python main.py "Build a modern AI SaaS landing page" --skip-install
```

To require CrewAI strictly and fail if it is missing:

```bash
export WEBBUILDER_REQUIRE_CREWAI=true
```

## CLI Options

```bash
python main.py "prompt"                     # Build a project
python main.py --check                      # Health check
python main.py --skip-install               # Skip npm install/build
python main.py --project-dir sandbox/myapp  # Custom output directory
python main.py -v "prompt"                  # Verbose logging
```

## Available Templates

| Template | Framework | CSS |
|----------|-----------|-----|
| `vite_react_saas` | Vite + React + TypeScript | TailwindCSS |
| `nextjs_saas` | Next.js App Router | TailwindCSS |
| `vite_vue` | Vite + Vue 3 | TailwindCSS |
| `static_html` | Pure HTML/CSS | Custom CSS |

## Engineering Rules Implemented

- CrewAI agents do not directly write random files.
- All writes are constrained to the sandbox root.
- Templates are preferred over blank-page generation.
- Context passed to models stays small.
- Debugging is iterative and error driven.
- Terminal commands are allowlisted through project tooling.
- Output is sanitized to prevent ANSI injection.
- File sizes are limited to prevent disk exhaustion.
