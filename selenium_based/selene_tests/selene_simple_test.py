#TODO selene tests
import unittest2
from selene import config
from selene import browser
from selene.api import *
from selene.browsers import BrowserName


class GoogleTest(unittest2.TestCase):
    def setUp(self):
        config.browser_name = BrowserName.CHROME

    def test_step_1(self):
        browser.open_url("https://google.com")

    def test_step_2(self):
        s("#q").set_value("Instrumenty  dolnej półki").press_enter()
