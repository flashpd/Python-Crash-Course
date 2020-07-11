import unittest
from city_functions import get_city_country

class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted = get_city_country('Santiago', 'Chile')
        self.assertEqual(formatted, 'Santiago, Chile')

unittest.main()