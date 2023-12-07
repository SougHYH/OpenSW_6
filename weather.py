from opsdroid.matchers import match_regex

import aiohttp


async def get_weather(config):
    base_url = "http://api.openweathermap.org/data/2.5/"
    api_url = "weather?q={}&units={}&appid={}".format(
        config['city'], config['unit'], config['api-key'])

    async with aiohttp.ClientSession() as session:
        response = await session.get(base_url + api_url)
        
    return await response.json()


@match_regex(r'!weather', case_sensitive=False)
async def tell_weather(opsdroid, config, message):

    weather = await get_weather(config)
    temp = weather['main']['temp']
    humidity = weather['main']['humidity']
    #city = weather['name']
    #status = weather['weather'][0]['description'].title()
    
    await message.respond("현재 기온은 {} 도이며, 습도는 {}% 입니다! "
                          "for today".format(temp, humidity))