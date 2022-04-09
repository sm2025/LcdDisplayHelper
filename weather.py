# import the module
import python_weather
import asyncio
from datetime import datetime
import time
import sys
# sys.path.append(".")
import displayHelper as dh


displayHelper = dh.DisplayHelper()

async def getweather():
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)
    weather = await client.find("Guttenberg, NJ")
    result =  weather.current
    # close the wrapper once done
    await client.close()
    return result

if __name__ == "__main__":
    now = datetime.now()
    current_hr = now.strftime("%H")
    current_min = now.strftime("%M")

    loop = asyncio.get_event_loop()
    resultWeather = loop.run_until_complete(getweather())

    temperature = resultWeather.temperature
    forecast = resultWeather.sky_text
    wind = resultWeather.wind_speed
    humidity = resultWeather.humidity
    

    displayObjects = []
    displayForecast = displayObjects.append(dh.DisplayObject(forecast, "yellow", 50, (0,0)))
    displayTime = displayObjects.append(dh.DisplayObject(str(wind), "yellow", 100, (60,20)))
    displayTime = displayObjects.append(dh.DisplayObject(str(humidity), "yellow", 100, (60,60)))
    displayTemperature =displayObjects.append(dh.DisplayObject(str(temperature), "mediumpurple", 150, (0,20)))

    displayHelper.completeDisplay(displayObjects)
    displayHelper.exitDisplay(); 
    
