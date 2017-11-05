import unittest

from metal import *

class TestMetal(unittest.TestCase):
    name = "TestMetal"
    price = 10

    def setUp(self):
        self.metal = Metal(self.name, self.price)

    def tearDown(self):
        Metal.remove_all_metals()
        self.metal = None

    def test_metal_creation(self):
        self.assertFalse(self.metal is None)
        self.assertEqual(self.metal.name, self.name)
        self.assertEqual(self.metal.price, self.price)

    def test_metal_creation_with_digit_as_name(self):
        new_name = 3
        metal = Metal(new_name, self.price)
        self.assertFalse(metal is None)
        self.assertEqual(metal.name, new_name)
        self.assertEqual(metal.price, self.price)

    def test_metal_creation_with_string_as_price(self):
        new_price = "test"
        metal = Metal(self.name, new_price)
        self.assertFalse(metal is None)
        self.assertEqual(metal.name, self.name)
        self.assertEqual(metal.price, new_price)

    def test_metal_metals_register(self):
        self.assertEqual(Metal.get_num_metals(), 1)
        # add another metal to make sure we are storing all metals
        new_name = "TestMetal1"
        new_price = 15
        Metal(new_name, new_price)
        self.assertEqual(Metal.get_num_metals(), 2)

    def test_metal_get_price(self):
        self.assertEqual(Metal.get_price(self.name), self.price)
        # add another metal to make sure we get the right price for each
        new_name = "TestMetal2"
        new_price = 20
        Metal(new_name, new_price)
        self.assertEqual(Metal.get_price(new_name), new_price)
        self.assertEqual(Metal.get_price(self.name), self.price)

if __name__ == '__main__':
    unittest.main()