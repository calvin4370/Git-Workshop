"""Generate an API key for the simulated workshop API."""

from secrets import token_urlsafe

KEY_PREFIX = "git_ws_"


def generate_key() -> str:
    """Return a cryptographically random simulated API key."""
    return f"{KEY_PREFIX}{token_urlsafe(32)}"


if __name__ == "__main__":
    print(generate_key())
