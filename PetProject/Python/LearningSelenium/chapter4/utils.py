import unittest
from selenium.webdriver.support.ui import WebDriverWait
from __builtin__ import classmethod

class Helpers():
    def wait_for_spinner(driver):
        # element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//*[@style="display: block;"]'))
        element = WebDriverWait(driver, 30).until_not(lambda x: x.find_element_by_xpath('//*[@style="display: block;"]').is_displayed())
        return element

    def field(self, unittest, locator, key_data):
        unittest.assertTrue(locator.is_displayed() and locator.is_enabled())
        locator.send_keys(key_data)

    def is_element_enable(self, unittest, locator):
        unittest.assertTrue(locator.is_displayed() and locator.is_enabled())


