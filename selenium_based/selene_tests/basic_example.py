from selene.api import *
import unittest2 as unittest
from selene import config
from selene.browsers import *
from selenium.webdriver.common.keys import Keys
from time import sleep



class TestTodoMVC(unittest.TestCase):

    def test_selene_demo(self):
        config.browser_name = BrowserName.CHROME
        browser.open_url('https://todomvc4tasj.herokuapp.com')

        tasks = ss("#todo-list>li")
        active_tasks = tasks.filtered_by(have.css_class("active"))

        s("#new-todo").should(be.blank)

        for task_text in ["1", "2", "3"]:
            sleep(0.7)
            s("#new-todo").set(task_text).press_enter()

        tasks.should(have.exact_texts("1", "2", "3")).should_each(have.css_class("active"))
        s("#todo-count").should(have.text('3'))

        tasks[2].s(".toggle").click()
        active_tasks.should(have.texts("1", "2"))
        active_tasks.should(have.size(2))

        tasks.filtered_by(have.css_class("completed")).should(have.texts("3"))

        s(by.link_text("Active")).click()
        tasks[:2].should(have.texts("1", "2"))
        tasks[2].should(be.hidden)

        s("#toggle-all").click()
        s("#clear-completed").click()
        tasks.should(be.empty)