# import the module
import python_weather
import asyncio
from datetime import datetime
import time
# import sys
# sys.path.append(".")
import displayHelper as dh
from PIL import Image
import os, random

displayHelper = dh.DisplayHelper()

async def getweather():
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)
    weather = await client.find("Guttenberg, NJ")
    result =  weather.current
    # close the wrapper once done
    await client.close()
    return result



def sendWeatherToDisplay(displayHelper):
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
    displayObjects.append(dh.DisplayObject(forecast, "white", 50, (0,0)))
    displayObjects.append(dh.DisplayObject(str(wind), "yellow", 100, (60,20)))
    displayObjects.append(dh.DisplayObject(str(humidity), "yellow", 100, (60,60)))
    displayObjects.append(dh.DisplayObject(str(temperature), "white", 150, (0,20)))

    displayHelper.completeDisplay(displayObjects)


def sendPictureToDisplay():
    fileDir = "/media/saroj/SMTEST/Photos/springWalk/"
    file = random.choice(os.listdir(fileDir)) 
    img = Image.open(fileDir+file)
    width, height = img.size
    # displayDim = (displayHelper.disp.height, displayHelper.disp.width)
    if (width>height):
        newWidth = 320
        newHeight = int(320/width*height)
    else: 
        newHeight = 240
        newWidth = int(240/height*width)
    newsize = (newWidth, newHeight)
    img = img.resize(newsize)
    #print("******"+ str(newsize[0]) + "****" + str(newsize[1]))
    reducedImagePath = "/media/saroj/SMTEST/python/test2.jpg"
    img.save(reducedImagePath)
    displayHelper.displayImage()

if __name__ == "__main__":
    for i in range(1):
        #sendWeatherToDisplay(displayHelper)
        #time.sleep(5)  
        sendPictureToDisplay()
        #time.sleep(5)
   
    displayHelper.exitDisplay() 
    
