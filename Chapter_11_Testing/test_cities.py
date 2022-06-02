import unittest
from city_functions import fortmated_city


class CityTestCase(unittest.TestCase):
    """Test for 'city_funtions.py'."""

    def test_city_country(self):
        """Do city-country like 'Santiago, Chile.' works?"""
        formatted_city_country = fortmated_city('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile.')
    
    def test_city_country_population(self):
        """Do city-country like 'Santiago, Chile - population 5000000' works?"""
        formatted_city_country_population = fortmated_city('santiago', 'chile', 5000000)
        self.assertEqual(formatted_city_country_population, 'Santiago, Chile - population 5000000.')

if __name__ == '__main__':
    unittest.main()
