# Web

AI full-stack autonomous web engineering scaffold using CrewAI, local Ollama models, template retrieval, sandboxed file writing, terminal execution, validation, and an automated debug loop.

## What This MVP Does

- Turns a user prompt into structured requirements.
- Plans a React/Tailwind webpage architecture.
- Retrieves a high-quality starter template.
- Generates project files into `sandbox/generated-app`.
- Runs install/build checks when Node tooling is available.
- Captures terminal errors and asks a debugger agent for repair patches.
- Retries validation up to a configurable limit.

## Project Layout

```text
agents/       Agent definitions and prompts
tasks/        Workflow task wrappers
tools/        Sandboxed file, terminal, scan, package, and error tools
templates/    Reusable project templates
sandbox/      Generated applications live here
webbuilder/   Core orchestration runtime
main.py       CLI entry point
```

## Requirements

- Python 3.10+
- Ollama running locally
- CrewAI installed from `requirements.txt`
- Recommended local models:
  - `qwen2.5:1.5b`
  - `qwen2.5:3b`
  - `qwen2.5-coder:3b`
  - Optional stronger debugger: `qwen2.5-coder:7b`
- Node.js and npm for generated frontend validation

## Quick Start

```powershell
pip install -r requirements.txt
python main.py "Build a modern AI SaaS landing page with pricing and contact sections"
```

The generated app is written to:

```text
sandbox/generated-app
```

## Configuration

Set environment variables if needed:

```powershell
$env:OLLAMA_HOST = "http://localhost:11434"
$env:OLLAMA_TIMEOUT = "180"
$env:WEBBUILDER_RETRY_LIMIT = "2"
$env:WEBBUILDER_DEBUGGER_MODEL = "qwen2.5-coder:7b"
```

CrewAI is enabled by default. For local template smoke tests without CrewAI/Ollama, you can temporarily run:

```powershell
$env:WEBBUILDER_USE_CREWAI = "false"
python main.py "Build a modern AI SaaS landing page" --skip-install
```

To require CrewAI strictly and fail if it is missing:

```powershell
$env:WEBBUILDER_REQUIRE_CREWAI = "true"
```

## Engineering Rules Implemented

- CrewAI agents do not directly write random files.
- All writes are constrained to the sandbox root.
- Templates are preferred over blank-page generation.
- Context passed to models stays small.
- Debugging is iterative and error driven.
- Terminal commands are allowlisted through project tooling.
