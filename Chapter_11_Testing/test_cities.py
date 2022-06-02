import unittest
from city_functions import fortmated_city


class CityTestCase(unittest.TestCase):
    """Test for 'city_funtions.py'."""

    def test_city_country(self):
        """Do city-country like 'Santiago, Chile.' works?"""
        formatted_city_country = fortmated_city('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile.')

if __name__ == '__main__':
    unittest.main()
