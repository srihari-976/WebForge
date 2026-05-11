from __future__ import annotations

import os
from dataclasses import dataclass

from webbuilder.config import CONFIG
from webbuilder.health import ensure_ollama_model_available
from webbuilder.json_utils import parse_json_object
from webbuilder.models import AgentOutput, JsonDict
from webbuilder.ollama_client import OllamaClient, OllamaUnavailable


os.environ.setdefault("OTEL_SDK_DISABLED", "true")
os.environ.setdefault("CREWAI_DISABLE_TELEMETRY", "true")


class CrewAIUnavailable(RuntimeError):
    """Raised when CrewAI cannot run the agent task."""


@dataclass(frozen=True)
class LocalAgent:
    name: str
    role: str
    goal: str
    backstory: str
    model: str
    system_prompt: str
    fallback: JsonDict

    @property
    def full_system_prompt(self) -> str:
        return (
            f"Role: {self.role}\n"
            f"Goal: {self.goal}\n"
            f"Backstory: {self.backstory}\n\n"
            f"{self.system_prompt}"
        )

    def run_json(self, prompt: str, client: OllamaClient) -> AgentOutput:
        if CONFIG.use_crewai:
            try:
                return self._run_json_with_crewai(prompt)
            except CrewAIUnavailable:
                if CONFIG.require_crewai:
                    raise

        try:
            raw = client.generate(self.model, prompt=prompt, system=self.full_system_prompt)
        except OllamaUnavailable:
            raw = ""
        data = parse_json_object(raw, self.fallback)
        return AgentOutput(raw=raw, data=data)

    def _run_json_with_crewai(self, prompt: str) -> AgentOutput:
        try:
            from crewai import Agent, Crew, LLM, Process, Task
        except ImportError as exc:
            raise CrewAIUnavailable("CrewAI is not installed. Run: pip install -r requirements.txt") from exc

        try:
            ensure_ollama_model_available(self.model)
            llm = LLM(
                model=f"ollama/{self.model}",
                base_url=CONFIG.ollama_host,
                temperature=0.2,
                timeout=CONFIG.ollama_timeout,
            )
            crew_agent = Agent(
                role=self.role,
                goal=self.goal,
                backstory=self.backstory,
                llm=llm,
                function_calling_llm=llm,
                verbose=False,
                allow_delegation=False,
                max_iter=5,
                max_retry_limit=0,
            )
            task = Task(
                description=(
                    f"{self.system_prompt}\n\n"
                    f"{prompt}\n\n"
                    "Return valid JSON only. Do not include markdown fences."
                ),
                expected_output="A single valid JSON object.",
                agent=crew_agent,
            )
            crew = Crew(
                agents=[crew_agent],
                tasks=[task],
                process=Process.sequential,
                verbose=False,
            )
            result = crew.kickoff()
        except Exception as exc:
            raise CrewAIUnavailable(str(exc)) from exc

        raw = getattr(result, "raw", str(result)).strip()
        data = parse_json_object(raw, self.fallback)
        return AgentOutput(raw=raw, data=data)
