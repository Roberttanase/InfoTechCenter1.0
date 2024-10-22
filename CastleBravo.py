print("\n**********************************\n")

print("Gasoline Branch")

import random
from time import sleep

def gasLevelGauge():
     gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
     return random.choice(gasLevelList)

def gasStations():
     gasStationList = ["VP","Shell","Meijer","Sams Club","Marathon","Mobile","Speedway","Circle K"]
     return random.choice(gasStationList)

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),2)
    milesToGasStationQuarterTank = round(random.uniform(25.1,50),2)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("\n***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is very low, checking GPS for closest gas station")
        sleep(2)
        print("The closest gas station is",gasStations(),"which is",milesToGasStationLow,"miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter of a tank, checking GPS for best gas station")
        sleep(2)
        print("The closest gas station is",gasStations(),"which is",milesToGasStationQuarterTank,"miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is a half a tank full, which is plenty to get to your destination.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is a three quarter tank full, which is plenty to get to your destination.")
    else:
        print("Your gas tank is full!")

gasLevelAlert()