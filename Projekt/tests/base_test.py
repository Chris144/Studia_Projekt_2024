import unittest
from datetime import time, datetime

from selenium import webdriver
from PIL import ImageGrab

"""
Base test for each page
"""


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://skleptest.pl/")
        self.driver.implicitly_wait(10)

    def screenshot(self):
        datetime.now()
        screenDatetime = datetime.now().strftime('%d-%m-%Y-%H-%M-%S')
        self.driver.save_screenshot(f"../screen_tests/screenshot-{screenDatetime}.png")

    def tearDown(self):
        self.driver.quit()
