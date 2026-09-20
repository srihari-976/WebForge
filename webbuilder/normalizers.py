from __future__ import annotations

from typing import Any

from webbuilder.models import JsonDict
from webbuilder.prompt_parser import (
    extract_features_from_prompt,
    extract_website_type_from_prompt,
    extract_sections_from_prompt,
    extract_color_from_prompt,
)


def _label(value: Any, fallback: str) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        for key in ("name", "page_name", "component_name", "title", "label"):
            found = value.get(key)
            if isinstance(found, str):
                return found
    return fallback


def _string_list(value: Any, fallback: list[str]) -> list[str]:
    if not isinstance(value, list):
        return fallback
    labels = [_label(item, "") for item in value]
    return [label for label in labels if label] or fallback


def normalize_requirements(data: JsonDict, prompt: str = "") -> JsonDict:
    normalized = dict(data)
    normalized["user_prompt"] = prompt
    normalized["website_type"] = _label(normalized.get("website_type"), "landing_page")
    normalized["pages"] = _string_list(normalized.get("pages"), ["home"])
    normalized["components"] = _string_list(
        normalized.get("components"),
        ["Navbar", "Hero", "Features", "Pricing", "Contact", "Footer"],
    )
    normalized["features"] = _string_list(normalized.get("features"), [])
    normalized["theme"] = _label(normalized.get("theme"), "modern")
    normalized["framework"] = _label(normalized.get("framework"), "Vite React")
    normalized["style_notes"] = _label(normalized.get("style_notes"), "polished responsive design")

    if prompt:
        if not normalized["features"] or normalized["features"] == [""]:
            prompt_features = extract_features_from_prompt(prompt)
            if prompt_features:
                normalized["features"] = prompt_features

        prompt_type = extract_website_type_from_prompt(prompt)
        if normalized["website_type"] == "landing_page" and prompt_type != "website":
            normalized["website_type"] = prompt_type

    return normalized


def normalize_plan(data: JsonDict, prompt: str = "") -> JsonDict:
    normalized = dict(data)
    normalized["layout"] = _label(normalized.get("layout"), "modern_saas")
    normalized["primary_color"] = _label(normalized.get("primary_color"), "blue")
    normalized["sections"] = _string_list(normalized.get("sections"), ["hero", "features", "pricing", "contact"])
    normalized["component_tree"] = _string_list(
        normalized.get("component_tree"),
        ["App", "Navbar", "Hero", "FeatureGrid", "Pricing", "Contact", "Footer"],
    )
    normalized["responsive_rules"] = _string_list(
        normalized.get("responsive_rules"),
        ["mobile-first", "single column on small screens", "multi-column desktop sections"],
    )

    if prompt:
        prompt_color = extract_color_from_prompt(prompt)
        if normalized["primary_color"] == "blue" and prompt_color != "blue":
            normalized["primary_color"] = prompt_color

        prompt_sections = extract_sections_from_prompt(prompt)
        if len(prompt_sections) > 2:
            normalized["sections"] = prompt_sections

    return normalized
