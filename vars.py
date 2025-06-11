#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "18579024"))
API_HASH = environ.get("API_HASH", "124981da628d86e21ee492da77cd4037")
BOT_TOKEN = environ.get("BOT_TOKEN", "7985589417:AAF0zkj96lSooMNBYxE8ya88VMZFB0euJz0")
OWNER = int(environ.get("OWNER", "7726207129"))
CREDIT = "𝄟⃝‌🐬🇳‌ɪᴋʜɪʟ𝄟⃝🐬"
AUTH_USER = os.environ.get('AUTH_USERS', '7726207129').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
