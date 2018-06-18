# from base_page import TestMethods
from selenium import webdriver
from random import randint
from selenium.webdriver.support import expected_conditions as EC
import unittest
import argparse
import logging
import sys
import nose
# from edit_functions import EditFunctions
# edit_instance = EditFunctions()
from selenium.webdriver.common.keys import Keys

# Global variables
# DEFAULT_WEB_DRIVER = webdriver.Chrome()
DEFAULT_HOST = 'https://tetra-qa.strikersoft.com/operational'
DEFAULT_PASSWORD = '12345+'
DEFAULT_LOGIN = 'tetra-support@strikersoft.com'
DEFAULT_EXECUTABLE = webdriver.Chrome
CONFIG_TEST_CLIENT = "Test_client_Robottest"
login_field_id = "login"
password_field_id = 'password'

CLIENT_MANAGEMENT_MENU = '//*[@id="bs-example-navbar-collapse-6"]/ul/li[6]/a'
CLIENT_MANAGEMENT_CLIENT_DETAILS_LISTMENU = 'clientDict2'
locator_select_client_list = 's2id_autogen1_search'

# Local variables
LOCATOR_CLIENT_MANAGEMENT_REGIONS_MENU = 'step_5'
LOCATOR_CLIENT_MANAGEMENT_LANDLORDS_MENU = 'step_6'

buttonAdd = 'buttonAdd'
locator_search_field_regions = '//*[@id="dict-table_filter"]/label/input'
locator_edit_button_regions =  '//*[@id="dict-table"]/tbody/tr/td[4]/a[1]'
locator_delete_button_regions =   '//*[@id="dict-table"]/tbody/tr/td[4]/a[2]'
LOCATOR_CODE_FIELD =               'record.code'
LOCATOR_NAME_FIELD =               'record.name'
LOCATOR_NOTE_FIELD =               'record.note'
LOCATOR_SAVE_BUTTON =              'submit'
edit_random_value = randint(10 ** (5 - 1), (10 ** 5) - 1)

class CreateDictionaries(unittest.TestCase):
    def setUp(self):

    # create a new session
      self.driver = webdriver.Chrome()
      self.driver.implicitly_wait(30)
      self.driver.maximize_window()

    # login as superuser
      driver = self.driver
      self.driver.get(DEFAULT_HOST)
      self.login_field = self.driver.find_element_by_id(login_field_id)
      self.login_field.send_keys(DEFAULT_LOGIN)
      self.pass_field = self.driver.find_element_by_id(password_field_id)
      self.pass_field.send_keys(DEFAULT_PASSWORD)
      self.submit_button = self.driver.find_element_by_xpath("//*[@id='loginForm']/button")
      self.submit_button.click()
    def random(self):
        return edit_random_value

    def test_create_regions(self):
        client_management_menu = self.driver.find_element_by_xpath(CLIENT_MANAGEMENT_MENU)
        client_management_menu.click()
        client_management_menu_list = self.driver.find_element_by_id(CLIENT_MANAGEMENT_CLIENT_DETAILS_LISTMENU)
        client_management_menu_list.click()
        select_client = self.driver.find_element_by_id(locator_select_client_list)
        select_client.send_keys(CONFIG_TEST_CLIENT)
        select_client.send_keys(Keys.ENTER)
        assert CONFIG_TEST_CLIENT in self.driver.page_source
        open_current_step = self.driver.find_element_by_id(LOCATOR_CLIENT_MANAGEMENT_REGIONS_MENU)
        open_current_step.click()
        assert "Regions" in self.driver.page_source
        button_add = self.driver.find_element_by_id(buttonAdd)
        button_add.click()
        code_field = self.driver.find_element_by_id(LOCATOR_CODE_FIELD)
        code_field.send_keys(edit_random_value)
        name_field = self.driver.find_element_by_id(LOCATOR_NAME_FIELD)
        name_field.send_keys(edit_random_value)
        note_field = self.driver.find_element_by_id(LOCATOR_NOTE_FIELD)
        note_field.send_keys(edit_random_value)
        save_button = self.driver.find_element_by_id(LOCATOR_SAVE_BUTTON)
        save_button.click()
        assert "Regions" in self.driver.page_source
    def test_create_landlord(self):
        client_management_menu = self.driver.find_element_by_xpath(CLIENT_MANAGEMENT_MENU)
        client_management_menu.click()
        client_management_menu_list = self.driver.find_element_by_id(CLIENT_MANAGEMENT_CLIENT_DETAILS_LISTMENU)
        client_management_menu_list.click()
        select_client = self.driver.find_element_by_id(locator_select_client_list)
        select_client.send_keys(CONFIG_TEST_CLIENT)
        select_client.send_keys(u'\ue007')
        assert CONFIG_TEST_CLIENT in self.driver.page_source
        open_current_step = self.driver.find_element_by_id(LOCATOR_CLIENT_MANAGEMENT_LANDLORDS_MENU)
        open_current_step.click()
        assert "Landlords" in self.driver.page_source
        button_add = self.driver.find_element_by_id(buttonAdd)
        button_add.click()
        code_field = self.driver.find_element_by_id(LOCATOR_CODE_FIELD)
        code_field.send_keys(edit_random_value)
        name_field = self.driver.find_element_by_id(LOCATOR_NAME_FIELD)
        name_field.send_keys(edit_random_value)
        note_field = self.driver.find_element_by_id(LOCATOR_NOTE_FIELD)
        note_field.send_keys(edit_random_value)
        save_button = self.driver.find_element_by_id(LOCATOR_SAVE_BUTTON)
        save_button.click()
        assert "Landlords" in self.driver.page_source



    # def tearDown(self):
    # # close the browser window
    #     self.driver.quit()

    if __name__ == '__main__':
        unittest.main(verbosity=2)