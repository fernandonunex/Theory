class User():
    """A simple attempt to represent a user"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")

    def greet_user(self):
        print(f"Welcome, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


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