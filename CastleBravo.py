import random  # For random selection of gas levels and gas stations
from time import sleep  # To add delays for simulating processing time

# Print a separator and a header
print("\n**********************************\n")
print("Gasoline Branch")


# Function to simulate gas level gauge
def gasLevelGauge():
    return random.choice(["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"])


# Function to simulate available gas stations
def gasStations():
    return random.choice(["VP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"])


# Function to display gas level alerts
def gasLevelAlert():
    gasLevelIndicator = gasLevelGauge()  # Get current gas level
    gasStation = gasStations()  # Find the nearest gas station once

    if gasLevelIndicator == "Empty":
        print("\n***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2)  # Simulate processing time
        print("Calling Triple AAA for emergency fuel assistance.")
    elif gasLevelIndicator == "Low":
        miles = round(random.uniform(1, 25), 2)
        print(f"Your gas tank is very low. The closest gas station is {gasStation}, {miles} miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        miles = round(random.uniform(25.1, 50), 2)
        print(f"Your gas tank is a quarter full. The closest gas station is {gasStation}, {miles} miles away.")
    elif gasLevelIndicator in ["Half Tank", "Three Quarter Tank"]:
        print(f"Your gas tank is {gasLevelIndicator.lower()}, which is plenty to reach your destination.")
    else:  # Full Tank
        print("Your gas tank is full!")


# Call the function to run the gas level alert system
gasLevelAlert()
