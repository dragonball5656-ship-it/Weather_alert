import requests
from datetime import datetime, timezone, timedelta

JST = timezone(timedelta(hours=9))

# 松阪市の座標
MATSUSAKA_LAT = 34.5781
MATSUSAKA_LON = 136.5270


def get_forecast(api_key: str) -> dict:
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "lat": MATSUSAKA_LAT,
        "lon": MATSUSAKA_LON,
        "appid": api_key,
        "units": "metric",
        "lang": "ja",
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def parse_today_weather(data: dict) -> dict:
    today = datetime.now(JST).date()

    today_items = [
        item for item in data["list"]
        if datetime.fromtimestamp(item["dt"], tz=JST).date() == today
    ]

    if not today_items:
        raise ValueError("今日の天気データが見つかりませんでした")

    temps = [item["main"]["temp"] for item in today_items]
    description = today_items[0]["weather"][0]["description"]

    return {
        "description": description,
        "temp_max": max(temps),
        "temp_min": min(temps),
    }
