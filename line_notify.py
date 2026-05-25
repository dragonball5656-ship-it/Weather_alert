import requests

LINE_PUSH_URL = "https://api.line.me/v2/bot/message/push"


def send_message(channel_access_token: str, user_id: str, text: str) -> None:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {channel_access_token}",
    }
    payload = {
        "to": user_id,
        "messages": [{"type": "text", "text": text}],
    }
    response = requests.post(LINE_PUSH_URL, headers=headers, json=payload, timeout=10)
    response.raise_for_status()
