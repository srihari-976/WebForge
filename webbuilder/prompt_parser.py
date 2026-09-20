from __future__ import annotations

import re
from webbuilder.models import JsonDict

KEYWORD_FEATURES: dict[str, list[str]] = {
    "ecommerce": ["Product catalog", "Shopping cart", "Secure checkout", "Order tracking"],
    "ecommerce_store": ["Product catalog", "Shopping cart", "Secure checkout", "Order tracking"],
    "store": ["Product catalog", "Shopping cart", "Secure checkout", "Order tracking"],
    "shop": ["Product catalog", "Shopping cart", "Secure checkout", "Order tracking"],
    "portfolio": ["Project showcase", "About section", "Contact form", "Responsive gallery"],
    "blog": ["Article listings", "Category filtering", "Search functionality", "Comment system"],
    "saas": ["Dashboard", "User authentication", "Pricing plans", "API integration"],
    "landing_page": ["Hero section", "Feature highlights", "Call to action", "Testimonials"],
    "landing": ["Hero section", "Feature highlights", "Call to action", "Testimonials"],
    "dashboard": ["Data visualization", "Real-time metrics", "User management", "Settings panel"],
    "forum": ["Thread creation", "User profiles", "Category sorting", "Moderation tools"],
    "chat": ["Real-time messaging", "User presence", "Message history", "File sharing"],
    "social": ["User profiles", "News feed", "Content sharing", "Like and comment"],
    "education": ["Course listings", "Progress tracking", "Quiz system", "Certificate generation"],
    "fitness": ["Workout tracker", "Progress charts", "Goal setting", "Meal planning"],
    "restaurant": ["Menu display", "Online ordering", "Reservation system", "Delivery tracking"],
    "real_estate": ["Property listings", "Search filters", "Map view", "Agent contact"],
    "healthcare": ["Appointment booking", "Patient records", "Doctor profiles", "Telehealth"],
    "music": ["Playlist management", "Audio player", "Artist profiles", "Lyrics display"],
    "travel": ["Destination search", "Booking system", "Itinerary planner", "Review ratings"],
}

KEYWORD_FEATURES_LOWERCASE: dict[str, list[str]] = {k.lower(): v for k, v in KEYWORD_FEATURES.items()}

SECTION_KEYWORDS: dict[str, list[str]] = {
    "hero": ["hero", "header", "banner", "main", "top", "landing"],
    "features": ["feature", "capability", "benefit", "what we offer"],
    "pricing": ["price", "pricing", "plan", "tier", "cost", "subscription"],
    "testimonials": ["testimonial", "review", "feedback", "what people say"],
    "contact": ["contact", "get in touch", "reach out", "email", "support"],
    "about": ["about", "our story", "team", "company"],
    "gallery": ["gallery", "portfolio", "showcase", "images", "photos"],
    "faq": ["faq", "questions", "help", "support"],
    "newsletter": ["newsletter", "subscribe", "updates", "email list"],
    "footer": ["footer", "bottom"],
    "stats": ["stats", "numbers", "metrics", "achievements"],
    "cta": ["call to action", "cta", "get started", "sign up"],
}


def extract_features_from_prompt(prompt: str) -> list[str]:
    prompt_lower = prompt.lower()
    all_features: list[str] = []
    for keyword, features in KEYWORD_FEATURES_LOWERCASE.items():
        if keyword in prompt_lower:
            all_features.extend(features)

    words = re.findall(r'\b\w+\b', prompt_lower)
    seen: set[str] = set()
    unique: list[str] = []
    for f in all_features:
        if f.lower() not in seen:
            seen.add(f.lower())
            unique.append(f)
    return unique[:6]


def extract_website_type_from_prompt(prompt: str) -> str:
    prompt_lower = prompt.lower()
    for keyword in KEYWORD_FEATURES_LOWERCASE:
        if keyword in prompt_lower:
            return keyword.replace("_", " ").title()
    return "website"


def extract_sections_from_prompt(prompt: str) -> list[str]:
    prompt_lower = prompt.lower()
    found: list[str] = ["hero"]
    for section, keywords in SECTION_KEYWORDS.items():
        if section == "hero":
            continue
        for kw in keywords:
            if kw in prompt_lower:
                if section not in found:
                    found.append(section)
                break
    if "features" not in found:
        found.append("features")
    if "contact" not in found:
        found.append("contact")
    return found


def extract_color_from_prompt(prompt: str) -> str:
    prompt_lower = prompt.lower()
    color_names = ["blue", "purple", "green", "red", "orange"]
    for color in color_names:
        if color in prompt_lower:
            return color
    return "blue"
