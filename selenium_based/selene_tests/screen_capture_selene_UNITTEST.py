import allure
from selene.browsers import BrowserName
from wand.image import Image
from selene import config
from selene import browser
from selene.api import *

import os
import unittest2 as unittest


"""
Use with:
(for WINDOWS)
python -m pytest unittest2_simple_test.py --alluredir ./results/$(Get-Date -Format g | foreach {$_ -replace ":", "."})/$(Get-Date -Format o | foreach {$_ -replace ":", "."})


"""

class ScreenCapture(unittest.TestCase):
    STAGING_URL = "http://www.yahoo.com"
    PRODUCTION_URL = "http://www.yahoo.com"
    # PRODUCTION_URL = "http://www.google.com"

    driver = None

    def setUp(self):
        config.browser_name = BrowserName.CHROME

    def compare_files(self, file_name_1, file_name_2):
        images = [
            Image(filename=os.path.join(
                os.path.dirname(
                    os.path.realpath(__file__)),
                'screenshots',
                file_name))
            for file_name in [file_name_1,
                              file_name_2]
        ]

        image, something = images[0].compare(images[1], metric="absolute")

        with image.convert('png') as converted:
            converted.save(filename='converted.png')
            print("SOMETHING")
            print(something)

    def screenshot(self, url, file_name):
        print("Capturing", url, "screenshot as", file_name, "...")
        print("before opening")
        browser.open_url(url)
        print("after opening")
        browser.driver().set_window_size(1024, 768)
        print("SAVING HERE:", os.path.join(os.path.dirname(os.path.realpath(__file__)), 'screenshots', file_name))
        browser.driver().get_screenshot_as_file(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), 'screenshots', file_name))
        print("Done.")

    def capture_screens(self):
        self.screenshot(self.STAGING_URL, 'screen_staging.png')
        self.screenshot(self.PRODUCTION_URL, 'screen_production.png')
        self.compare_files('screen_staging.png', 'screen_production.png')

    # @allure.MASTER_HELPER.testcase("", name="Testing if True is True - it should be...")
    def test_compare_images(self):
        self.capture_screens()


if __name__ == '__main__':
    unittest.main()