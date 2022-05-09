class Restaurant():
    """A simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Initialize restaurant_name and cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """Just print the attributes"""
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}\n")

    def open_restaurant(self):
        """Prints that the restaurant is open"""
        print("The restaurant is open!!!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_number):
        if increment_number > 0:
            self.number_served += increment_number
        else:
            print("Please enter a valid number")

class IceCreamStand(Restaurant):
    """A class that inherits form Restaurant"""
    def __init__(self, restaurant_name, flavors, number_served=0):
        super().__init__(restaurant_name, number_served)
        self.flavors = flavors