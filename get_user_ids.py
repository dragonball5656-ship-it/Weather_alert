import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")
headers = {"Authorization": f"Bearer {token}"}

r = requests.get("https://api.line.me/v2/bot/followers/ids", headers=headers)
r.raise_for_status()

user_ids = r.json().get("userIds", [])
print(f"友だち数: {len(user_ids)} 人")
for uid in user_ids:
    print(f"  User ID: {uid}")
