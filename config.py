"""Configuration load and setup for the bot."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASEDIR = Path(Path(__file__).parent).resolve()
load_dotenv(BASEDIR / ".env")

TIMEZONE = "Europe/Amsterdam"

# Bot setup
VERSION = "0.4.0"
PREFIX = "!"
BOT_NAME = "Dutch Drone Squad"
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
OWNER_ID = int(os.getenv("OWNER_ID"))

# Discord Guild ID
GUILD_ID = int(os.getenv("GUILD_ID"))

# Discord roles IDs
ROOKIE_ROLE_ID = int(os.getenv("ROOKIE_ROLE_ID"))
ADVANCED_ROLE_ID = int(os.getenv("ADVANCED_ROLE_ID"))
ANALOG_ROLE_ID = int(os.getenv("ANALOG_ROLE_ID"))
DIGITAL_ROLE_ID = int(os.getenv("DIGITAL_ROLE_ID"))
RACING_ROLE_ID = int(os.getenv("RACING_ROLE_ID"))
FREESTYLE_ROLE_ID = int(os.getenv("FREESTYLE_ROLE_ID"))

# Twitch API
TWITCH_CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
TWITCH_CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")
TWITCH_CHANNEL_ID = int(os.getenv("TWITCH_CHANNEL_ID"))
