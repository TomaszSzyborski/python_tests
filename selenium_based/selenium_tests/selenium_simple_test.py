#TODO selenium_tests
import unittest2 as unittest
from webdriver_manager.chrome import ChromeDriver, ChromeDriverManager
from page_objects import PageObject, PageElement
from selenium import webdriver


class LoginPage(PageObject):
    username = PageElement(id_='username')
    password = PageElement(name='password')
    login = PageElement(css='input[type="submit"]')


class TestSimple(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://example.com")

    def tearDown(self):
        self.driver.close()

    def test_simple(self):
        page = LoginPage(self.driver)
        page.username = 'secret'
        page.password = 'squirrel'
        assert page.username.text == 'secret'
        page.login.click()
