"""Exercise client for the simulated local LLM API."""

import sys


API_KEY = ""


def main() -> int:
    if len(sys.argv) != 2:
        print('Usage: python api_testing.py "<prompt>"')
        return 2

    if not API_KEY:
        print("Error: API key is required.")
        return 1

    print("The simulated API is not configured yet.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
