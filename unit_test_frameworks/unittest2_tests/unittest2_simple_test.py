import unittest2
import pytest
import allure

"""
Use with:
(for WINDOWS)
python -m pytest unittest2_simple_test.py --alluredir ./results/$(Get-Date -Format g | foreach {$_ -replace ":", "."})/$(Get-Date -Format o | foreach {$_ -replace ":", "."})


"""


@allure.story('Your Story here')
@allure.feature('Your Feature here')
class SimpleUnitTest(unittest2.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @allure.testcase("", name="Testing if True is True - it should be...")
    def test_should_pass(self):
        """
        This test should pass
        :return:
        """
        self.assertTrue(
            True,
            msg="True should be true - it's an axiom."
        )

    @allure.testcase("", "Testing if True is False - it shouldn't be...")
    def test_should_fail(self):
        """
        This test should raise and Assertion error,
        that should be caught by assertRaises method
        and therefore pass gracefully
        :return:
        """
        self.assertRaises(
            AssertionError,
            self.assertTrue,
            False,
            msg="True shouldn't be false - it's an axiom."
        )


class TestWithSteps(unittest2.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @allure.step("Test step 1 title")
    def test_step_1(self):
        self.assertNotEqual(
            1,
            2
        )

    @allure.step("Test step 2 title")
    def test_step_2(self):
        self.assertEqual(
            2,
            2
        )

    @allure.step("Test step 3 title")
    def test_step_3(self):
        self.assertAlmostEqual(
            1.65,
            1.62,
            places=1
        )
