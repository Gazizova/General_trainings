import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import os
import nose
import argparse
import logging
import sys
import time

__author__ = 'yuriy@strikersoft.com'
__description__ = "Tetra test"

DEFAULT_WEB_DRIVER = 'Chrome'
#DEFAULT_HOST = 'https://api.tetrapops.com'
DEFAULT_HOST = 'https://tetra-dev.strikersoft.com'
DEFAULT_PASSWORD = '12345+'
DEFAULT_EXECUTABLE = './chromedriver'
TEST_PARAMS = ['', __file__, '-v', '--all-modules', '--with-xunit', '--xunit-file=test_report.xml']

class TestMethods(unittest.TestCase):
    logging.basicConfig(stream=sys.stdout, level=logging.WARN,
                        format='%(asctime)s - '
                               '%(name)s - '
                               '%(levelname)s - '
                               '%(message)s')

    def __init__(self, test_name, **kwargs):
        super(TestMethods, self).__init__(test_name)
        parser = argparse.ArgumentParser(description=__description__)
        parser.add_argument('--host', required=False, help='Host address', default=DEFAULT_HOST)
        parser.add_argument('--user', required=False, help='User to use')
        parser.add_argument('--password', required=False, help='password to use', default=DEFAULT_PASSWORD)
        parser.add_argument('--webdriver', required=False, help='webdriver to use', default=DEFAULT_WEB_DRIVER)
        parser.add_argument(
            '--executable',
            required=False,
            help='webdriver executable, must match the webdriver',
            default=DEFAULT_EXECUTABLE
        )
        self.enviroment_args, unknown = parser.parse_known_args()

    def setUp(self):
        self.browser = getattr(
            webdriver, self.enviroment_args.webdriver.capitalize()
        )(executable_path=self.enviroment_args.executable)
        self.browser.implicitly_wait(5)
        self.browser.get('{}/operational/login.html'.format(self.enviroment_args.host))
        self.browser.maximize_window()

    def login_as_operator(self):
        login_field = self.browser.find_element_by_xpath(
            '//*[@id="login"]')
        login_field.send_keys(
            'tetra-support@strikersoft.com')
        password_field = self.browser.find_element_by_xpath(
            '//*[@id="password"]')
        password_field.send_keys('12345+')
        sign_in = self.browser.find_element_by_xpath(
            '//*[@id="loginForm"]/button')
        sign_in.click()

    def login_as_consultant_1(self):
        login = self.browser.find_element_by_xpath(
            '//*[@id="login"]')
        login.send_keys(
            'consultant1@strikersoft.com')
        password_field = self.browser.find_element_by_xpath(
            '//*[@id="password"]')
        password_field.send_keys('12345+')
        sign_in = self.browser.find_element_by_xpath(
            '//*[@id="loginForm"]/button')
        sign_in.click()

    def login_qa_1(self):
        login = self.browser.find_element_by_xpath(
            '//*[@id="login"]')
        login.send_keys(
            'qa1@strikersoft.com')
        password_field = self.browser.find_element_by_xpath(
            '//*[@id="password"]')
        password_field.send_keys('12345+')
        sign_in = self.browser.find_element_by_xpath(
            '//*[@id="loginForm"]/button')
        sign_in.click()

    def check_alert(self):
        if EC.alert_is_present:
            print('Alert Exists')
        else:
            print('No alert')
    def value_is_required(self):
        this_value_is_required = self.browser.find_element_by_xpath(
            '//*[@id="parsley-id-6"]/li')
        self.assertEqual(this_value_is_required.text, 'This value is required.')

    def add_file(self):
        self.browser.find_element_by_id('actionFile').send_keys(
            '{}{}images.jpg'.format(os.getcwd(), os.sep))
        image_field = self.browser.find_element_by_xpath(
            '//*[@id="task-actions-addon"]/div/div/ul/li/label/div')
        self.assertEqual(image_field.text, 'images.jpg')
    def send_comments(self):
        comment_field = self.browser.find_element_by_xpath(
                 '//*[@id="record.comment"]')
        comment_field.send_keys('comment from Python')




if __name__ == '__main__':
    nose.run(defaultTest="", argv=TEST_PARAMS)