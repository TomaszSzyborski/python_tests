#TODO selene tests
import unittest2
from selene import config
from selene import browser
from selene.api import *


class GoogleTest(unittest2.TestCase):
    def step_1(self):
        browser.open_url("https://google.com")

    def step_2(self):
        s("#q").set_value("Instrumenty  dolnej półki").press_enter()
