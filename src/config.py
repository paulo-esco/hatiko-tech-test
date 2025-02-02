import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ALLOWED_TELEGRAM_USERS = {7512738152}

API_AUTH_TOKEN = os.getenv("API_AUTH_TOKEN")

IMEI_API_URL = os.getenv("IMEI_API_URL")
IMEI_API_TOKEN = os.getenv("IMEI_API_TOKEN")
