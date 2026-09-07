import os

api_id = int(os.environ.get("API_ID", 36349640))
api_hash = os.environ.get("API_HASH", "c3ce4116ac51baa0432b65127a2f92dc")
bot_token = os.environ.get("BOT_TOKEN", "8899188686:AAF5T83Kxae7THkIgbqInKIvRa4QEuAoOEw")
auth_users = [int(x.strip()) for x in os.environ.get("AUTH_USERS", "1910301357").split(",") if x.strip().isdigit()]

if not api_id: raise ValueError("Set API_ID env var!")
if not api_hash: raise ValueError("Set API_HASH env var!")
if not bot_token: raise ValueError("Set BOT_TOKEN env var!")
if not auth_users: raise ValueError("Set AUTH_USERS env var!")
