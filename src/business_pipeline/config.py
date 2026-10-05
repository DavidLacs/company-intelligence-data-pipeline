from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[2]

load_dotenv(PROJECT_ROOT / ".env")


SEC_BASE_URL = "https://data.sec.gov"

SEC_USER_AGENT = os.getenv("SEC_USER_AGENT")

if not SEC_USER_AGENT:
    raise RuntimeError(
        "SEC_USER_AGENT is not configured. "
        "Set it in the project's .env file."
    )


REQUEST_TIMEOUT_SECONDS = 30

MAX_RETRIES = 3

RETRY_BACKOFF_SECONDS = 1.0

MIN_REQUEST_INTERVAL_SECONDS = 0.2