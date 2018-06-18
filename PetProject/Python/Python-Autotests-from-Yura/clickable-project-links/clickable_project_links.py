import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import sys
import argparse
import nose

__author__ = 'yuriy@strikersoft.com'
__description__ = "Tetra test"

DEFAULT_WEB_DRIVER = 'Chrome'
#DEFAULT_HOST = 'https://api.tetrapops.com'
DEFAULT_HOST = 'https://tetra-dev.strikersoft.com'
DEFAULT_PASSWORD = '12345+'
DEFAULT_EXECUTABLE = './chromedriver'

TEST_PARAMS = ['', __file__, '-v', '--all-modules', '--with-xunit', '--xunit-file=test_report.xml']

# random_value = randint(10**(5-1), (10**5)-1)
# now = datetime.datetime.now().timestamp()

class Link_test(unittest.TestCase):
    " Project stages tests for tetra"
    logging.basicConfig(stream=sys.stdout, level=logging.WARN,
                        format='%(asctime)s - '
                               '%(name)s - '
                               '%(levelname)s - '
                               '%(message)s')

    def __init__(self, test_name, **kwargs):
        super(Link_test, self).__init__(test_name)
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

    def login(self):
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

    def login_as_consultant(self):
        login_field = self.browser.find_element_by_xpath(
            '//*[@id="login"]')
        login_field.send_keys(
            'consultant1@strikersoft.com')
        password_field = self.browser.find_element_by_xpath(
            '//*[@id="password"]')
        password_field.send_keys('12345+')
        sign_in = self.browser.find_element_by_xpath(
            '//*[@id="loginForm"]/button')
        sign_in.click()
    def test_dev_Prism_admin(self):
        self.browser.get(
            '{}/operational/login.html'.format(self.enviroment_args.host))
        self.login()

        ref_num = self.browser.find_element_by_id('refNum')
        ref_num.send_keys('ASS-2016211172943')
        search_field = self.browser.find_element_by_xpath(
            '//*[@id="downloadProjects-form"]/div/div[1]/div[2]/div[3]/div/button')
        search_field.click()
        project_link_dev = WebDriverWait(self.browser, 50).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '//*[@id="tasks-table"]/tbody/tr/td[7]/a')))
        project_link_dev.click()
        project_info = self.browser.find_element_by_xpath(
            '//*[@id="model"]/div[1]/div[1]/div[1]/div[1]/h2')
        self.assertIn(project_info.text, 'Project info')
    def test_qa_Prism_admin(self):
        self.browser.get(
            '{}/operational/login.html'.format(self.enviroment_args.host))
        self.login()
        ref_num = self.browser.find_element_by_id('refNum')
        ref_num.send_keys('B-53098')
        search_field = self.browser.find_element_by_xpath(
            '//*[@id="downloadProjects-form"]/div/div[1]/div[2]/div[3]/div/button')
        search_field.click()
        project_link_qa = WebDriverWait(self.browser, 50).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '//*[@id="tasks-table"]/tbody/tr/td[7]/a')))
        client_name = self.browser.find_element_by_xpath(
            '//*[@id="tasks-table"]/tbody/tr/td[8]/span')
        self.assertIn(client_name.text, 'Sam Sailor')
    # def test_dev_Prism_consultant(self):
    #     self.browser.get(
    #         '{}/operational/login.html'.format(self.enviroment_args.host))
    #     self.login_as_consultant()
    #     ref_num = self.browser.find_element_by_id('refNum')
    #     ref_num.send_keys('ASS-2016211172943')
    #     search_field = self.browser.find_element_by_xpath(
    #         '//*[@id="downloadProjects-form"]/div/div[1]/div[2]/div[3]/div/button')
    #     search_field.click()
    #     project_link_dev = WebDriverWait(self.browser, 50).until(
    #         EC.element_to_be_clickable((By.XPATH,
    #                                     '//*[@id="tasks-table"]/tbody/tr/td[7]/a')))
    #     project_link_dev.click()
    #     project_info = self.browser.find_element_by_xpath(
    #         '//*[@id="model"]/div[1]/div[1]/div[1]/div[1]/h2')
    #     self.assertIn(project_info.text, 'Project info')
    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    nose.run(defaultTest="", argv=TEST_PARAMS)