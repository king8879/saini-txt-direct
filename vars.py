#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22923037"))
API_HASH = environ.get("API_HASH", "dfb3666878b3851460a58461c5a50f5b")
BOT_TOKEN = environ.get("BOT_TOKEN", "7395464729:AAGRu6eikdkGCuyhvxQaEWXV98rRZdRQQs4")
OWNER = int(environ.get("OWNER", "7576541713"))
CREDIT = "𝄟⃝‌🐬🇳‌ɪᴋʜɪʟ𝄟⃝🐬"
AUTH_USER = os.environ.get('AUTH_USERS', '7576541713').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
