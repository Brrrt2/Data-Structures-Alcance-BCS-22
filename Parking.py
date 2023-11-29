class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.QList = [None] * capacity
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.isFull():
            print("The list is full or overflow")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.QList[self.rear] = item
        self.size = self.size + 1
        print("% s add to list " % str(item))

    def queueFront(self):
        if self.isEmpty():
            print("Queue is empty.")
        print("Front item is ", self.QList[self.front])

    def queueRear(self):
        if self.isEmpty():
            print("Queue is empty.")
        print("Rear item is ", self.QList[self.rear])

    def dequeue(self):
        if self.isEmpty():
            print("The list is empty.")
            return None
        dq = self.QList[self.front]
        self.QList[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size = self.size - 1
        print("% s removed from list" % str(dq))
        return dq


class ParkingSimulator:
    def __init__(self, capacity):
        self.parking_queue = Queue(capacity)

    def enter_parking_lot(self, plate_number, arrival_time):
        if not self.parking_queue.isFull():
            car_info = {'plate_number': plate_number, 'arrival_time': arrival_time, 'departure_time': None}
            self.parking_queue.enqueue(car_info)
            print(f"Car with plate number {plate_number} has entered the parking lot.")
        else:
            print("Parking lot is full. Cannot park the car.")

    def exit_parking_lot(self, plate_number, departure_time):
        if not self.parking_queue.isEmpty():
            for index, car_info in enumerate(self.parking_queue.QList):
                if car_info is not None and car_info['plate_number'] == plate_number:
                    self.parking_queue.QList[index] = None
                    self.parking_queue.size -= 1
                    car_info['departure_time'] = departure_time
                    print(f"Car with plate number {plate_number} has left the parking lot.")
                    print(f"Departure Time: {departure_time}")
                    return

            print(f"Car with plate number {plate_number} not found in the parking lot.")
        else:
            print("Parking lot is empty.")

    def display_parking_lot(self):
        if not self.parking_queue.isEmpty():
            print(" ")
            print("Parking Lot:")
            print(" ")
            print("<-- Exit ", end="")

            for car_info in self.parking_queue.QList:
                if car_info is not None:
                    print(f"| {car_info['plate_number']} ", end="")
                else:
                    print("| Empty ", end="")

            print("| <-- Entrance")
        else:
            print("Parking lot is empty.")

if __name__ == '__main__':
    parking_simulator = ParkingSimulator(5)

    while True:
        print("\nParking Simulator Menu:")
        print("1. Enter Parking Lot")
        print("2. Exit Parking Lot")
        print("3. Display Parking Lot")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            plate_number = input("Enter the plate number of the car: ")
            arrival_time = input("Enter the arrival time of the car: ")
            parking_simulator.enter_parking_lot(plate_number, arrival_time)

        elif choice == '2':
            plate_number = input("Enter the plate number of the car: ")
            departure_time = input("Enter the departure time of the car: ")
            parking_simulator.exit_parking_lot(plate_number, departure_time)

        elif choice == '3':
            parking_simulator.display_parking_lot()

        elif choice == '4':
            print("Exiting the Parking Simulator. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
