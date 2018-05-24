from wand.image import Image
from wand.display import display
from selenium import webdriver
import os

from webdriver_manager.chrome import ChromeDriverManager


class ScreenCapture:
    STAGING_URL = 'http://www.yahoo.com'
    PRODUCTION_URL = 'http://www.google.com'
    driver = None

    def __init__(self):
        self.set_up()
        self.capture_screens()
        self.clean_up()


    def set_up(self):
        # self.driver = webdriver.PhantomJS()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def clean_up(self):
        self.driver.close()

    def capture_screens(self):
        self.screenshot(self.STAGING_URL, 'screen_staging.png')
        self.screenshot(self.PRODUCTION_URL, 'screen_production.png')
        self.comare_files('screen_staging.png', 'screen_production.png')

    def screenshot(self, url, file_name):
        print("Capturing", url, "screenshot as", file_name, "...")
        self.driver.get(url)
        self.driver.set_window_size(1024, 768)
        print("SAVING HERE:", os.path.join(os.path.dirname(os.path.realpath(__file__)), 'screenshots', file_name))
        # self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'screenshots', file_name))
        # self.driver.get_screenshot_as_png()
        self.driver.get_screenshot_as_file(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'screenshots', file_name))
        print("Done.")


    def comare_files(self, file_name_1, file_name_2):
        img_1 = Image(filename=os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                            'screenshots',
                                            file_name_1))

        img_2 = Image(filename=os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                            'screenshots',
                                            file_name_2))

        # Image(img_1.compare(img_2)).save(filename="asdasdasd.png")
        with (img_1.compare(img_2))[0].convert('png') as converted:
            converted.save(filename='converted.png')




if __name__ == '__main__':
    ScreenCapture()
