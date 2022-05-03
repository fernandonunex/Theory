from curses.ascii import US


class User():
    """A simple attempt to represent a user"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    
    def describe_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")

    
    def greet_user(self):
        print(f"Welcome, {self.first_name}!")


def run():
    user_1 = User("Tobias", "Smith")
    user_2 = User("Friedrich", "Lattice")


    user_1.describe_user()
    user_2.greet_user()

if __name__ == "__main__":
        run()