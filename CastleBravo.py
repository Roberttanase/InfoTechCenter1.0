print("\n********************************\n")
print("Weather Branch\n")

# Import Libraries
import random
from time import sleep

# Function to simulate weather forecast
def weather():
    weatherForecast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]
    return random.choice(weatherForecast)

# Get a random weather condition
weatherAlert = weather()

# Dictionary to map weather conditions to alarm and speed adjustments
weather_responses = {
    "snowy": {"alarm": 30, "speed": 55},
    "blizzard": {"alarm": 45, "speed": 45},
    "rainy": {"alarm": 10, "speed": 65},
    "windy": {"alarm": 5, "speed": 65},
    "icy": {"alarm": 60, "speed": 35}
}

# Function to handle the vehicle's response to the weather condition
def vehicleResponseSystem():
    if weatherAlert in weather_responses:
        response = weather_responses[weatherAlert]
        print(f"\nThe National Weather Service has updated our alarm by {response['alarm']} minutes because"
              f" of the forecast of {weatherAlert} weather conditions.")
        sleep(1)
        print(f"\nVRS system has been engaged only allowing you to drive {response['speed']}mph.")
    else:  # Handle sunny or any other weather condition not listed above
        print(f"\nThe National Weather Service is calling for {weatherAlert} skies, drive carefully to get to your"
              " destination!")
        sleep(1)
        print("\nVRS system has been disengaged")

# Call the vehicle response system
vehicleResponseSystem()
