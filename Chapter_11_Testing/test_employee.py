import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Test for the class Employee"""

    def setUp(self):
        """Create an employee with a first - last name and salary"""
        self.employee_1 = Employee('Fernando', 'Nunez', 50000)

    def test_give_default_raise(self):
        self.employee_1.give_raise()
        self.assertEqual(55000, self.employee_1.salary)

    def test_give_custom_raise(self):
        self.employee_1.give_raise(10000)
        self.assertEqual(60000, self.employee_1.salary)

if __name__ == '__main__':
    unittest.main()
