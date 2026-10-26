"""Shared configuration for the course.

API keys and model names are loaded from environment variables, not hard-coded.
"""

import os

# Set AIE_MODEL to use a different model.
# Example: export AIE_MODEL=gemini-3.5-flash
DEFAULT_MODEL = "gemini-3.5-flash-lite"
MODEL = os.getenv("AIE_MODEL", DEFAULT_MODEL)


def api_error_message(status: int, detail: str = "") -> str:
    """Return a student-friendly explanation for an HTTP status code."""
    if status == 429:
        return "Rate limit reached. Wait about a minute, then try again."
    if status == 503:
        return "The model is busy (503). Wait a moment, then try again."
    if status in (400, 401, 403, 404):
        return f"There is a problem with the API key or model name ({status}): {detail}"
    return f"API error ({status}): {detail}"


def get_api_key() -> str:
    """Return GEMINI_API_KEY, or exit with setup instructions if it is missing."""
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise SystemExit(
            "GEMINI_API_KEY is not set.\n"
            "1. Add GEMINI_API_KEY under GitHub Settings > Codespaces > Secrets, and select your fork.\n"
            "2. If you added it after starting the Codespace, restart the Codespace."
        )
    return key
