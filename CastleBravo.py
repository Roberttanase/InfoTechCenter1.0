# Print a separator and a header
print("\n**********************************\n")
print("Gasoline Branch")

# Import the required libraries
import random  # For random selection of gas levels and gas stations
from time import sleep  # To add delays for simulating processing time

# Function to simulate gas level gauge
def gasLevelGauge():
    # List of possible gas levels
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    # Randomly select a gas level from the list
    return random.choice(gasLevelList)

# Function to simulate available gas stations
def gasStations():
    # List of gas stations
    gasStationList = ["VP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"]
    # Randomly select a gas station from the list
    return random.choice(gasStationList)

# Function to check gas level and alert user
def gasLevelAlert():
    # Generate a random distance to the closest gas station when the tank is low
    milesToGasStationLow = round(random.uniform(1, 25), 2)  # Distance for low gas levels
    milesToGasStationQuarterTank = round(random.uniform(25.1, 50), 2)  # Distance for quarter tank
    # Get the current gas level from the gasLevelGauge function
    gasLevelIndicator = gasLevelGauge()

    # Handle different gas levels with respective actions
    if gasLevelIndicator == "Empty":
        print("\n***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2)  # Simulate time delay
        print("Calling Triple AAA")  # Simulate an emergency response

    elif gasLevelIndicator == "Low":
        print("Your gas tank is very low, checking GPS for closest gas station")
        sleep(2)  # Simulate time delay
        print("The closest gas station is", gasStations(), "which is", milesToGasStationLow, "miles away.")

    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter of a tank, checking GPS for best gas station")
        sleep(2)  # Simulate time delay
        print("The closest gas station is", gasStations(), "which is", milesToGasStationQuarterTank, "miles away.")

    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is half a tank full, which is plenty to get to your destination.")

    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is three quarter tank full, which is plenty to get to your destination.")

    else:
        print("Your gas tank is full!")  # When the gas tank is full, no need to refuel

# Call the gasLevelAlert function to start the alert system
gasLevelAlert()
