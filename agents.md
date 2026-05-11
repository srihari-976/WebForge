# Autonomous Web Engineering Platform

This project is a multi-agent AI system built using CrewAI.

Purpose:
Build full-stack web applications autonomously from user prompts.

## Tech Stack

- CrewAI
- Ollama
- Qwen2.5-Coder
- FastAPI
- Next.js
- TailwindCSS

## Agent Architecture

### Orchestrator Agent
Responsible for:
- workflow management
- task delegation
- execution ordering

### Requirement Analyzer Agent
Responsible for:
- extracting structured requirements
- identifying pages/components/features

### Frontend Agent
Responsible for:
- generating React/Next.js code
- Tailwind styling
- reusable UI components

### Backend Agent
Responsible for:
- FastAPI generation
- CRUD APIs
- authentication

### Debugger Agent
Responsible for:
- reading terminal logs
- fixing build errors
- retrying builds

## Engineering Rules

- Never overwrite files directly
- Always generate patches/diffs
- Use templates whenever possible
- Keep context minimal
- Avoid generating entire projects in one step

## Folder Structure

agents/
tasks/
tools/
templates/
sandbox/

## Coding Standards

- Use TailwindCSS
- Use functional React components
- Use modular architecture
- Use reusable components
- Use async FastAPI routes

## Tool Usage

### FileWriterTool
Writes generated files safely.

### TerminalTool
Runs:
- npm install
- npm run dev
- pip install

### ErrorReaderTool
Reads terminal logs and stack traces.

## Model Routing

- qwen2.5:1.5b → orchestration
- qwen2.5-coder:3b → frontend/backend
- qwen2.5-coder:7b → debugging

## Goal

The system should:
1. Understand prompts
2. Generate applications
3. Run builds
4. Fix errors autonomously
5. Provide live preview

## Documentation

Fetch CrewAI docs from:
https://docs.crewai.com/llms.txt