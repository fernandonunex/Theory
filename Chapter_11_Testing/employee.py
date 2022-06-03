class Employee():
    """Create a simple model of an employee"""

    def __init__(self, first_name, last_name, salary):
        """Ask basic information of an employee and salary"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount=5000):
        """Raise the annual salary"""
        self.salary += amount
