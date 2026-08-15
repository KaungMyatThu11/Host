# Copyright (C) @TheSmartBisnu
# Channel: https://t.me/itsSmartDev

from os import getenv
from time import time
from dotenv import load_dotenv

load_dotenv("config.env.local", override=False)
load_dotenv("config.env", override=False)


def _must_get(name: str) -> str:
    value = (getenv(name) or "").strip()
    if not value:
        raise ValueError(f"{name} is required")
    return value


def _validate_bot_token(token: str) -> str:
    if token.count(":") != 1:
        raise ValueError("BOT_TOKEN must be in format 123456:abcdef...")
    return token


class PyroConf(object):
    API_ID = int((getenv("API_ID") or "0").strip())
    API_HASH = _must_get("API_HASH")
    BOT_TOKEN = _validate_bot_token(_must_get("BOT_TOKEN"))
    SESSION_STRING = _must_get("SESSION_STRING")
    BOT_START_TIME = time()

    MAX_CONCURRENT_DOWNLOADS = max(1, int((getenv("MAX_CONCURRENT_DOWNLOADS") or "1").strip()))
    BATCH_SIZE = max(1, int((getenv("BATCH_SIZE") or "1").strip()))
    FLOOD_WAIT_DELAY = max(0, int((getenv("FLOOD_WAIT_DELAY") or "10").strip()))

    FORWARD_CHAT_ID = (getenv("FORWARD_CHAT_ID") or "").strip() or None


if PyroConf.API_ID <= 0:
    raise ValueError("API_ID must be a valid positive integer")
