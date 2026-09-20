from __future__ import annotations

from webbuilder.prompt_parser import (
    extract_features_from_prompt,
    extract_website_type_from_prompt,
    extract_sections_from_prompt,
    extract_color_from_prompt,
)


class TestPromptParser:
    def test_ecommerce_features(self) -> None:
        features = extract_features_from_prompt("Build an ecommerce store with a shopping cart")
        assert "Product catalog" in features
        assert "Shopping cart" in features

    def test_portfolio_features(self) -> None:
        features = extract_features_from_prompt("Create a portfolio site for a photographer")
        assert "Project showcase" in features
        assert "Responsive gallery" in features

    def test_blog_features(self) -> None:
        features = extract_features_from_prompt("Build a blog with article listings and search")
        assert "Article listings" in features
        assert "Search functionality" in features

    def test_saas_features(self) -> None:
        features = extract_features_from_prompt("Create a SaaS dashboard with authentication")
        assert "Dashboard" in features
        assert "User authentication" in features

    def test_website_type_ecommerce(self) -> None:
        wtype = extract_website_type_from_prompt("Build an ecommerce store")
        assert "ecommerce" in wtype.lower()

    def test_website_type_portfolio(self) -> None:
        wtype = extract_website_type_from_prompt("Create a photography portfolio")
        assert "portfolio" in wtype.lower()

    def test_website_type_saas(self) -> None:
        wtype = extract_website_type_from_prompt("Build a SaaS app")
        assert "saas" in wtype.lower()

    def test_website_type_default(self) -> None:
        wtype = extract_website_type_from_prompt("Build something cool")
        assert wtype == "website"

    def test_sections_pricing(self) -> None:
        sections = extract_sections_from_prompt("Build a landing page with pricing and testimonials")
        assert "pricing" in sections
        assert "testimonials" in sections
        assert "hero" in sections

    def test_sections_default(self) -> None:
        sections = extract_sections_from_prompt("Build a simple website")
        assert "hero" in sections
        assert "features" in sections
        assert "contact" in sections

    def test_color_purple(self) -> None:
        assert extract_color_from_prompt("Use a purple theme") == "purple"

    def test_color_green(self) -> None:
        assert extract_color_from_prompt("Make it green") == "green"

    def test_color_default(self) -> None:
        assert extract_color_from_prompt("Build a website") == "blue"

    def test_complex_prompt(self) -> None:
        prompt = "Build a fitness tracking app with dashboard, dark mode, and a purple theme"
        features = extract_features_from_prompt(prompt)
        assert "Workout tracker" in features
        assert "Progress charts" in features
        sections = extract_sections_from_prompt(prompt)
        assert "hero" in sections
        assert extract_color_from_prompt(prompt) == "purple"
        wtype = extract_website_type_from_prompt(prompt)
        assert wtype.lower() in ("fitness", "dashboard")
