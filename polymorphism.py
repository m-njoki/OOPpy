class Vehicle:
    # Move method
    def move(self):
        pass


# Subclasses
class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying.")

class Boat(Vehicle):
    def move(self):
        print("Sailing.")

# Creating objects for each subclass
vehicles = [Car(), Plane(), Boat()]

# Calling the move method for each object
for vehicle in vehicles:
    vehicle.move()