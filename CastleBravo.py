import sys  # Importing the sys module to access system-specific parameters and functions
import time  # Importing the time module to add delays (simulate loading time)

# ANSI escape sequences for colors
RESET = "\033[0m"  # Reset to default color
GREEN = "\033[32m"  # Green text
YELLOW = "\033[33m"  # Yellow text
RED = "\033[31m"  # Red text for warnings/errors

# Print the welcome message at the start with color
print(GREEN + "\nWelcome to InfoTechCenter V1.0\n" + RESET)

timeToSleep = 1.75 #variable to set the time library to 1.75 seconds when called
time.sleep(timeToSleep) #calling the time to sleep library with the variable timeToSleeps value

x = 0  # Initial counter for the number of iterations
ellipsis = 0  # Counter for the number of dots in the ellipsis animation

# Loop to simulate the booting process (runs 20 times)
while x != 20:
    x += 1  # Increment the counter for each iteration
    # Create the message that includes the animated ellipsis (increases the number of dots each time)
    message = (YELLOW + "InfoTech Center System Booting" + "." * ellipsis + RESET)

    # Increment the ellipsis counter for the next dot
    ellipsis += 1

    # Use sys.stdout.write to overwrite the current line with the new message
    sys.stdout.write("\r" + message)

    # Add a delay to slow down the loop, so the animation looks smooth
    time.sleep(0.75)

    # Reset the ellipsis counter after 3 dots, so it loops back to 0
    if ellipsis == 4:
        ellipsis = 0

# Once 20 iterations have passed, print the final message in green
if x == 20:
    print("\n\n" + GREEN + "Operating System Booted Up - Retina Scanned - Access Granted" + RESET)

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

