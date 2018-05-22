#TODO pyhamcrest assertions
from hamcrest import *
import unittest2 as unittest


class Biscuit:
    def __init__(self, flavour):
        self.flavour = flavour


class BiscuitTest(unittest.TestCase):

    def test_equals(self):
        the_biscuit = Biscuit('Ginger')
        my_biscuit = Biscuit('Ginger')
        assert_that(the_biscuit, equal_to(my_biscuit))


if __name__ == '__main__':
    unittest.main()
