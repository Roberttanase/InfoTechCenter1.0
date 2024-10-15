print("\n********************************\n")
print("Weather Branch\n")

# Import Libraries Here
import random  # 'random' module used to make random selections from a list
from time import sleep  # 'sleep' function will pause the execution for a given amount of seconds


# Function to simulate weather forecast
def weather():
    # List of possible weather conditions
    weatherForecast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]
    # Randomly select one condition from the list
    weatherCondition = random.choice(weatherForecast)
    # Return the randomly selected weather condition
    return weatherCondition


# Get a random weather condition by calling the weather() function
weatherAlert = weather()


# Function to handle the vehicle's response to the weather condition
def vehicleResponseSystem():
    # Check if the weather is snowy
    if weatherAlert == "snowy":
        # Print a message with a 30-minute alarm adjustment due to snowy weather
        print("\nThe National Weather Service has updated our alarm by 30 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)  # Pause for 1 second
        # Print a message that VRS system allows max 55mph speed
        print("\nVRS system has been engaged only allowing you to drive 55mph.")

    # Check if the weather is a blizzard
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated our alarm by 45 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 45mph.")

    # Check if the weather is rainy
    elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated our alarm by 10 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 65mph.")

    # Check if the weather is windy
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated our alarm by 5 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 65mph.")

    # Check if the weather is icy
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated our alarm by 60 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 35mph.")

    # If the weather is sunny or any other condition not listed above
    else:
        print("\nThe National Weather service is calling for", weatherAlert, "skies, drive carefully to get to your"
                                                                             " destination!")
        sleep(1)
        # Disengage the VRS system when weather is good
        print("\nVRS system has been disengaged")


# Call the vehicleResponseSystem function to execute the VRS response based on weather condition
vehicleResponseSystem()
