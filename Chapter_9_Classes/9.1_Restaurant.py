class Restaurant():
    """A simple attempt to model a dog"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    

    def describe_restaurant(self):
        """Just print the attributes"""
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    
    def open_restaurant(self):
        """Prints that the restaurant is open"""
        print("The restaurant is open!!!")


if __name__ == "__main__":
        my_restaurant = Restaurant("El huevon", "Mexican")

        print(my_restaurant.restaurant_name)
        print(my_restaurant.cuisine_type)

        my_restaurant.describe_restaurant()
        my_restaurant.open_restaurant()
