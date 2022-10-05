import os
from dotenv import load_dotenv

load_dotenv()

# Bot setup
VERSION = "0.2.0"
TESTING = os.getenv("TESTING", "false")
PREFIX = "!"
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
BOT_DEV_TOKEN = os.getenv("BOT_DEV_TOKEN", "")
OWNER_ID = int(os.getenv("OWNER_ID"))