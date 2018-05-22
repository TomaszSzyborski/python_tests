# Import stuff you need for the unit tests themselves to work
import random
import unittest2 as unittest


# Import stuff that you want to test.  Don't import extra stuff if you don't
# have to.

def answer():
    return random.randint(1, 10)




class School:
    def age(self):
        return 123
    def food(self):
        return "eatable"


class TestAnswer(unittest.TestCase):

    def test_type(self):
        "answer() returns an integer"
        self.assertEqual(type(answer()), int)

    def test_expected(self):
        "answer() returns 42"
        self.assertEqual(answer(), 42)


class TestSchool(unittest.TestCase):

    def test_food(self):
        school = School()
        self.assertEqual(school.food(), 'awful')

    def test_age(self):
        school = School()
        self.assertEqual(school.age(), 300)
