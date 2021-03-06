from users import User

class Admin(User):
    """A simple attempt to represent an Admin that inherits from User class"""

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


class Privileges():
    """A simple attempt to represent the privileges"""

    def __init__(self, privileges=['add post', 'delete post', 'ban user']) -> None:
        self.privileges = privileges

    def show_privileges(self):
        """A function that prints the privileges of a user"""
        print("The privileges are:")
        for privilege in self.privileges:
            print(f"--{privilege}")