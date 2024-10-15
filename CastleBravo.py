print("\n********************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

def weather():
    weatherForecast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition

weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nThe National Weather Service has updated our alarm by 30 minutes becuase"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 55mph.")
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated our alarm by 45 minutes becuase"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 45mph.")
    elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated our alarm by 10 minutes becuase"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 65mph.")
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated our alarm by 5 minutes becuase"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 65mph.")
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated our alarm by 60 minutes becuase"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 35mph.")
    else:
        print("\nThe National Weather service is calling for", weatherAlert, "skies, drive carefully to get to your"
        " destination!")
        sleep(1)
        print("\nVRS system has been disengaged")

vehicleResponseSystem()