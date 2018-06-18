from LearningSelenium.Python_2.base_login2 import LoginAsSuperuser2
from LearningSelenium.Python_2.uimap2 import Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

import unittest
from selenium import webdriver

import time

l = Locators()
class BaseTest(object):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        return driver

class CreateProject(unittest.TestCase):

    def login(self, user_login, user_pass):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        return driver
        driver.maximize_window()
        driver.get(l.LoginDataMap['url'])

        WebDriverWait(self.driver, 10).until(expected_conditions
                                             .visibility_of_element_located((By.ID, l.LoginDataMap['login_field'])))
        self.login_field = driver.find_element_by_id(l.LoginDataMap['login_field'])
        self.login_field.send_keys(user_login)


        WebDriverWait(self.driver, 10).until(expected_conditions
                                             .visibility_of_element_located((By.ID, l.LoginDataMap['password_field'])))
        self.pass_field = self.driver.find_element_by_id(l.LoginDataMap['password_field'])
        self.pass_field.send_keys(user_pass)


        self.submit_button = self.driver.find_element_by_xpath(l.LoginDataMap['login_button'])
        self.submit_button.click()

        WebDriverWait(self.driver, 10).until_not(
            lambda x: x.find_element_by_xpath('//*[@style="display: block;"]').is_displayed())
    def test_login_as_superuser(self):
        a = CreateProject()
        a.login(l.LoginDataMap['user_login'], l.LoginDataMap['user_pass'])
    def test_create_project(self):
        driver = self.driver
        self.project_menu = driver.find_element_by_id(l.DashboardMenuMap['projectTool'])
        self.assertTrue(self.project_menu.is_displayed() and self.project_menu.is_enabled())
        self.project_menu.click()
        time.sleep(2)

if __name__ == "__main__":
 unittest.main()
