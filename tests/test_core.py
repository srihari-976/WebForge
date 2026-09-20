from __future__ import annotations

import json
from pathlib import Path

from webbuilder.json_utils import parse_json_object
from webbuilder.normalizers import normalize_requirements, normalize_plan
from webbuilder.models import CommandResult, AgentOutput


class TestParseJsonObject:
    def test_valid_json(self) -> None:
        result = parse_json_object('{"key": "value"}', {})
        assert result == {"key": "value"}

    def test_json_in_markdown(self) -> None:
        text = '```json\n{"key": "value"}\n```'
        result = parse_json_object(text, {})
        assert result == {"key": "value"}

    def test_empty_string_returns_fallback(self) -> None:
        result = parse_json_object("", {"fallback": True})
        assert result == {"fallback": True}

    def test_non_dict_returns_fallback(self) -> None:
        result = parse_json_object("[1, 2, 3]", {"fallback": True})
        assert result == {"fallback": True}

    def test_no_json_returns_fallback(self) -> None:
        result = parse_json_object("no json here", {"fallback": True})
        assert result == {"fallback": True}

    def test_nested_json(self) -> None:
        text = 'Here is the result: {"a": {"b": 1}}'
        result = parse_json_object(text, {})
        assert result == {"a": {"b": 1}}


class TestNormalizeRequirements:
    def test_minimal_input(self) -> None:
        result = normalize_requirements({})
        assert result["website_type"] == "landing_page"
        assert result["pages"] == ["home"]
        assert result["theme"] == "modern"
        assert result["framework"] == "Vite React"
        assert isinstance(result["components"], list)
        assert isinstance(result["features"], list)

    def test_existing_values_preserved(self) -> None:
        data = {"website_type": "portfolio", "pages": ["home", "about"], "theme": "dark"}
        result = normalize_requirements(data)
        assert result["website_type"] == "portfolio"
        assert result["pages"] == ["home", "about"]
        assert result["theme"] == "dark"

    def test_dict_labels_extracted(self) -> None:
        data = {"website_type": {"name": "SaaS App"}}
        result = normalize_requirements(data)
        assert result["website_type"] == "SaaS App"

    def test_string_list_coercion(self) -> None:
        data = {"components": [{"component_name": "Nav"}, "Hero"]}
        result = normalize_requirements(data)
        assert "Nav" in result["components"]
        assert "Hero" in result["components"]


class TestNormalizePlan:
    def test_minimal_input(self) -> None:
        result = normalize_plan({})
        assert result["layout"] == "modern_saas"
        assert result["primary_color"] == "blue"
        assert isinstance(result["sections"], list)
        assert isinstance(result["component_tree"], list)
        assert isinstance(result["responsive_rules"], list)

    def test_existing_values_preserved(self) -> None:
        data = {"layout": "dashboard", "primary_color": "purple", "sections": ["nav", "sidebar"]}
        result = normalize_plan(data)
        assert result["layout"] == "dashboard"
        assert result["primary_color"] == "purple"
        assert result["sections"] == ["nav", "sidebar"]


class TestCommandResult:
    def test_ok_property(self) -> None:
        result = CommandResult(command=["npm", "run", "build"], cwd=Path("."), return_code=0, stdout="", stderr="")
        assert result.ok is True

    def test_not_ok(self) -> None:
        result = CommandResult(command=["npm", "run", "build"], cwd=Path("."), return_code=1, stdout="", stderr="error")
        assert result.ok is False

    def test_combined_output(self) -> None:
        result = CommandResult(command=[], cwd=Path("."), return_code=0, stdout="hello", stderr="world")
        assert "hello" in result.combined_output
        assert "world" in result.combined_output

    def test_combined_output_empty(self) -> None:
        result = CommandResult(command=[], cwd=Path("."), return_code=0, stdout="", stderr="")
        assert result.combined_output == ""


class TestAgentOutput:
    def test_creation(self) -> None:
        output = AgentOutput(raw='{"key": "value"}', data={"key": "value"})
        assert output.raw == '{"key": "value"}'
        assert output.data == {"key": "value"}
