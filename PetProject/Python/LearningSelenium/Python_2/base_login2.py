from selenium import webdriver

# from base_test import BaseTestCase
from uimap2 import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


l = Locators()

class LoginAsSuperuser2():
    def login(self, user_login, user_pass):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(l.LoginDataMap['url'])

        WebDriverWait(self.driver, 10).until(expected_conditions
                                             .visibility_of_element_located((By.ID, l.LoginDataMap['login_field'])))
        self.login_field = self.driver.find_element_by_id(l.LoginDataMap['login_field'])
        self.login_field.send_keys(user_login)


        WebDriverWait(self.driver, 10).until(expected_conditions
                                             .visibility_of_element_located((By.ID, l.LoginDataMap['password_field'])))
        self.pass_field = self.driver.find_element_by_id(l.LoginDataMap['password_field'])
        self.pass_field.send_keys(user_pass)


        self.submit_button = self.driver.find_element_by_xpath(l.LoginDataMap['login_button'])
        self.submit_button.click()

        WebDriverWait(self.driver, 10).until_not(
            lambda x: x.find_element_by_xpath('//*[@style="display: block;"]').is_displayed())

# a = LoginAsSuperuser2().login(l.LoginDataMap['user_login'], l.LoginDataMap['user_pass'])
