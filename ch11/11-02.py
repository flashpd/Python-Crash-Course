import unittest
from city_functions_2 import get_city_country

class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted = get_city_country('Santiago', 'Chile')
        self.assertEqual(formatted, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted = get_city_country('Santiago', 'Chile', 5000)
        self.assertEqual(formatted, 'Santiago, Chile - population 5000')

unittest.main()