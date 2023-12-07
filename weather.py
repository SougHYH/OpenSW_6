from opsdroid.matchers import match_regex
import aiohttp

# OpenWeatherMap API 토큰을 직접 코드에 설정
API_KEY = "531a92c10601431dfddc53dd76a4695a"
CITY = "Seoul"  # 서울로 고정

async def get_weather():
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": CITY, "units": "metric", "appid": API_KEY}

    async with aiohttp.ClientSession() as session:
        response = await session.get(base_url, params=params)
    
    return await response.json()

@match_regex(r'!weather', case_sensitive=False)
async def tell_weather(opsdroid, config, message):
    weather_data = await get_weather()

    if "main" in weather_data and "temp" in weather_data["main"]:
        temp = weather_data["main"]["temp"]
        weather_status = weather_data["weather"][0]["description"].title()
        humidity = weather_data["main"]["humidity"]

        response_message = (
            f"현재 서울의 기온은 {temp}°C 이고 "
            f"습도는 {humidity}% 입니다."
        )
        await message.respond(response_message)