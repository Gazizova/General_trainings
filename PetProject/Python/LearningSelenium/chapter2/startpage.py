import unittest
from selenium import webdriver
import HTMLTestRunner
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from __builtin__ import classmethod

class TestSearchTests(unittest.TestCase):

    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    @classmethod
    def setUp(self):
    # create a new  session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        self.driver.get("https://tetra-qa.strikersoft.com/operational")
        self.login_field = self.driver.find_element_by_id("login")
        self.login_field.send_keys("tetra-support@strikersoft.com")
        self.pass_field = self.driver.find_element_by_id("password")
        self.pass_field.send_keys("Qqq!1234")
        self.submit_button = self.driver.find_element_by_xpath("//*[@id='loginForm']/button")
        self.submit_button.click()

    def test_all_menu_present(self):
        self.driver.implicitly_wait(30)
        self.spinner = self.driver.find_element_by_xpath("//*[@style='display: block;']")
        menu = self.driver.find_elements_by_xpath("//*[@class='nav navbar-nav']/li")
        print (len(menu))
        self.assertEqual(len(menu), 6)
        self.assertGreater(len(menu), 5)

    def test_is_dashboard_date_present(self):
        self.assertTrue(self.driver.find_element_by_id("datefrom"))
        self.assertTrue(self.driver.find_element_by_id("dateto"))

    def test_is_dashboard_list_present(self):
        self.assertTrue(self.driver.find_element_by_id("clientList"))
        self.assertTrue(self.driver.find_element_by_id("property"))

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
 # unittest.main()
# if __name__ == '__main__':
 HTMLTestRunner.main()