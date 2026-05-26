from datetime import datetime, timezone, timedelta

JST = timezone(timedelta(hours=9))

WEATHER_EMOJI = {
    "晴": "☀️",
    "曇": "☁️",
    "雨": "🌧️",
    "雪": "❄️",
    "霧": "🌫️",
    "雷": "⛈️",
}


def _get_emoji(description: str) -> str:
    for keyword, emoji in WEATHER_EMOJI.items():
        if keyword in description:
            return emoji
    return "🌤️"


def build_message(description: str, temp_max: float, temp_min: float) -> str:
    today = datetime.now(JST).strftime("%m月%d日")
    emoji = _get_emoji(description)
    return (
        f"おはようございます！\n{today}の天気です\n"
        f"📍 三重県松阪市\n"
        f"{emoji} 天気：{description}\n"
        f"🌡 気温：{temp_max:.0f}℃/{temp_min:.0f}℃"
    )
