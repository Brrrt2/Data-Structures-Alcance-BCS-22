import time

numfloors = 5

currentfloor = 1
choosefloor = [1, 2, 3, 4, 5]

def elevator(targetfloor):
    global currentfloor
    if 1 <= targetfloor <= numfloors:
        while currentfloor != targetfloor:
            if currentfloor < targetfloor:
                currentfloor += 1
                time.sleep(1)
                print("Moving Up to Floor", currentfloor)
            else:
                currentfloor -= 1
                print("Moving down to Floor", currentfloor)
                time.sleep(1)
        print("You are at your destination")
    else:
        print("Invalid floor choice. Please select a floor between 1 and", numfloors)

def inputfloor():
    while True:
        try:
            floor_input = int(input("Enter Floor: "))
            return floor_input
        except ValueError:
            print("Error...Please input a valid Floor")

while True:
    print("Floor Choices:", choosefloor)
    targetfloor = inputfloor()
    elevator(targetfloor)
    another_floor = input("Do you want to go to another floor? (yes/no): ").lower()
    if another_floor != "yes":
        break
