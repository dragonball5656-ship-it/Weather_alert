import os
import sys
from dotenv import load_dotenv

from weather import get_forecast, parse_today_weather
from message import build_message
from line_notify import send_message

load_dotenv()


def main():
    weather_api_key = os.environ.get("WEATHER_API_KEY")
    line_token = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")
    line_user_ids_raw = os.environ.get("LINE_USER_IDS")

    missing = [k for k, v in {
        "WEATHER_API_KEY": weather_api_key,
        "LINE_CHANNEL_ACCESS_TOKEN": line_token,
        "LINE_USER_IDS": line_user_ids_raw,
    }.items() if not v]

    if missing:
        print(f"[ERROR] 環境変数が未設定です: {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)

    user_ids = [uid.strip() for uid in line_user_ids_raw.split(",") if uid.strip()]

    try:
        data = get_forecast(weather_api_key)
        weather = parse_today_weather(data)
        text = build_message(
            weather["description"],
            weather["temp_max"],
            weather["temp_min"],
        )
        for user_id in user_ids:
            send_message(line_token, user_id, text)
            print(f"通知を送信しました → {user_id}")
        print(text)
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
