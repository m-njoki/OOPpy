class Building:
    # Constructor to initialize the Building
    def __init__(self, name, height, location):
        self.name = name
        self.height = height
        self.location = location

    # Methods for the Building class
    def display(self):
        print(f"Building Name: {self.name}, Height: {self.height}m, Location: {self.location}")

    def calculate_area(self, base_area):
        return base_area * self.height
    

# Subclass
class ResidentialBuilding(Building):
    # Constructor to initialize the ResidentialBuilding
    def __init__(self, name, height, location, num_apartments):
        super().__init__(name, height, location)
        self.num_apartments = num_apartments

# Overriding the display method to include the no of apartments
    def display(self):
        super().display()
        print(f"Number of Apartments: {self.num_apartments}")


# Subclass
class CommercialBuilding(Building):
    # Constructor to initialize the CommercialBuilding
    def __init__(self, name, height, location, num_offices):
        super().__init__(name, height, location)
        self.num_offices = num_offices

    # Overriding the display method to include the number of offices
    def display(self):
        super().display()
        print(f"Number of Offices: {self.num_offices}")



# Creating objects
res_building = ResidentialBuilding("Sunset Apartments", 50, "Downtown", 100)

com_building = CommercialBuilding("Tech Tower", 120, "City Center", 50)

# Calling the display method for the objects
res_building.display()

com_building.display()
