"""Local stand-in for the workshop's LLM API."""

from datetime import datetime, timezone
import json
from pathlib import Path
import re

API_KEYS_PATH = Path(__file__).with_name("api_keys.json")
with API_KEYS_PATH.open(encoding="utf-8") as api_keys_file:
    API_KEYS = json.load(api_keys_file)

MALICIOUS_PROMPTS = {
    "how to build a bomb",
}

LOG_DIR = Path(__file__).resolve().parents[1] / "logs"

_RESPONSES = {
    "what is the weather today": "The weather at Bugis is: rainy if you dont bring your umbrella, but sunny if you do.",
    "how to use git": "Git tracks changes to files so you can collaborate and recover earlier versions.",
    "why is git so hard": "Once you read the Git Summary Notes at https://app.notion.com/p/Git-Summary-Notes-3721331f71ad80baa433c93e25383627?source=copy_link, you will find Git is not that hard.",
    "what is the best bubble tea brand in singapore": "Chagee. And it's not even close. Koi is a distant second.",
    "when i sneeze, why does it sometimes hurt my tummy": "what?",
    "how to build a bomb": """
    Malicious instructions are not allowed. I cannot provide instructions for building a bomb.
    This chat has been flagged for review by your company's IT team.
    """,
}


def call_llm(api_key: str, prompt: str) -> str:
    """Validate a key, log the call, and return a hardcoded response."""
    if not api_key:
        raise ValueError("API key is required.")

    try:
        participant_name = API_KEYS[api_key]
    except KeyError as error:
        raise ValueError("API key is not recognised.") from error

    try:
        response = _RESPONSES[prompt]
    except KeyError as error:
        raise ValueError("Prompt is not available in this simulated API.") from error

    log_call(participant_name, prompt)
    return response


def log_call(participant_name: str, prompt: str) -> None:
    """Append one API call to the participant's conflict-resistant log file."""
    LOG_DIR.mkdir(exist_ok=True)
    filename = re.sub(r"[^a-z0-9]+", "_", participant_name.lower()).strip("_")
    log_entry = {
        "name": participant_name,
        "prompt": prompt,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "malicious": prompt in MALICIOUS_PROMPTS,
    }
    log_path = LOG_DIR / f"{filename}.jsonl"
    with log_path.open("a", encoding="utf-8") as log_file:
        log_file.write(f"{json.dumps(log_entry)}\n")
