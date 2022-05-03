class Restaurant():
    """A simple attempt to model a dog"""

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

if __name__ == "__main__":
    my_restaurant = Restaurant("El huevon", "Mexican")
    your_restaurant = Restaurant("El tacon", "Peruan")
    her_restaurant = Restaurant("El devops", "Spanish")

    # print(my_restaurant.restaurant_name)
    # print(my_restaurant.cuisine_type)

    # my_restaurant.describe_restaurant()
    # your_restaurant.describe_restaurant()
    # her_restaurant.describe_restaurant()

    # Exercise 9.3
    print(my_restaurant.number_served)
    my_restaurant.number_served = 15
    print(my_restaurant.number_served)
    my_restaurant.set_number_served(20)
    print(my_restaurant.number_served)
    my_restaurant.increment_number_served(10)
    print(my_restaurant.number_served)
    my_restaurant.increment_number_served(10)
    print(my_restaurant.number_served)
    my_restaurant.increment_number_served(-15)

