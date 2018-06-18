import unittest
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
import time
from dashboard_locators import Locators
from utils import Helpers
from getrequests import Authenticate
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# from __builtin__ import classmethod
import datetime

l = Locators()

time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d-%H%M%S')


class popsDashboard(unittest.TestCase, Helpers):
    @classmethod
    def setUp(cls):
    # create a new  session
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

        cls.driver.get(l.server_url)
        cls.login_field = cls.driver.find_element_by_id("login")
        cls.login_field.send_keys("tetra-support@strikersoft.com")
        cls.pass_field = cls.driver.find_element_by_id("password")
        cls.pass_field.send_keys("Qqq!1234")
        cls.submit_button = cls.driver.find_element_by_xpath("//*[@id='loginForm']/button")
        cls.submit_button.click()

    def test_create_project(self):
        driver = self.driver
        WebDriverWait(driver, 10).until_not(
            lambda x: x.find_element_by_xpath('//*[@style="display: block;"]').is_displayed())

        # project menu: get and click
        self.project_menu = driver.find_element_by_id(l.projectTool)
        self.assertTrue(self.project_menu.is_displayed()and self.project_menu.is_enabled())
        self.project_menu.click()

        # create project click
        WebDriverWait(driver, 10).until(lambda el: el.find_element_by_id(l.CREATE_PROJECT))
        driver.find_element(By.ID, l.CREATE_PROJECT).click()

        # fill mandatory fields
        helper = Helpers()
        helper.field(self, driver.find_element(By.ID, l.project_code), time_stamp)
        helper.field(self, driver.find_element(By.ID, l.project_note), time_stamp)
        helper.field(self, driver.find_element(By.ID, l.project_address), time_stamp)
        helper.field(self, driver.find_element(By.ID, l.project_client), time_stamp)
        helper.field(self, driver.find_element(By.ID, l.project_contact), time_stamp)
        print (time_stamp)

        driver.find_element_by_id(l.project_add_button).click()


    def test_jss_stage(self):
        driver = self.driver
        WebDriverWait(driver, 10).until_not(
            lambda x: x.find_element_by_xpath('//*[@style="display: block;"]').is_displayed)

        helper = Helpers()
        helper.field(self, driver.find_element(By.ID, l.search_ref), time_stamp)
        driver.find_element_by_xpath('//*[@id="downloadProjects-form"]//*[@data-target="list"]').click()
        WebDriverWait(driver, 10).until_not(lambda el: el.find_element(By.XPATH, '//*[@id="tasks-table"]/tbody/tr[2]').is_displayed)
        time.sleep(2)
        project_ref_num = driver.find_element_by_xpath('//*[@id="tasks-table"]/tbody/tr/td[7]/a')
        project_ref_num.click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(l.project_code).is_displayed())
        assert driver.find_element(By.ID, l.project_code).is_displayed()

        auth = Authenticate()
        auth.delete_project(time_stamp)


    @classmethod
    def tearDown(cls):
        cls.driver.quit()
        # auth = Authenticate()
        # auth.delete_project(time_stamp)

if __name__ == "__main__":
 unittest.main()
