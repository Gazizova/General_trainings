from base_page import TestMethods
from selenium import webdriver
import argparse
import logging
import sys
import nose
from edit_functions import EditFunctions
edit_instance = EditFunctions()


# I am using python unittest for asserting cases.
# In this module, there should be test cases.

__author__ = 'yuriy@strikersoft.com'
__description__ = "Tetra test"

DEFAULT_WEB_DRIVER = 'Chrome'
#DEFAULT_HOST = 'https://api.tetrapops.com'
DEFAULT_HOST = 'https://tetra-qa.strikersoft.com'
DEFAULT_PASSWORD = '12345+'
DEFAULT_EXECUTABLE = webdriver.Chrome
TEST_PARAMS = ['', __file__, '-v', '--all-modules', '--with-xunit', '--xunit-file=test_report.xml']

class TestPages(TestMethods):

    logging.basicConfig(stream=sys.stdout, level=logging.WARN,
                        format='%(asctime)s - '
                               '%(name)s - '
                               '%(levelname)s - '
                               '%(message)s')

    def __init__(self, test_name, **kwargs):
        super(TestPages, self).__init__(test_name)
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
        self.driver =webdriver.Chrome()
        # self.driver.implicitly_wait(5)
        self.driver.get('https://tetra-qa.strikersoft.com/operational/login.html')
        self.driver.maximize_window()

    # def setUp(self):
    #     self.browser = getattr(
    #         webdriver, self.enviroment_args.webdriver.capitalize()
    #     )(executable_path=self.enviroment_args.executable)
    #     self.browser.implicitly_wait(5)
    #     self.browser.get('{}/operational/login.html'.format(self.enviroment_args.host))
    #     self.browser.maximize_window()

    def test_alogin(self):
        self.login_with_valid_user()

    # def test_create_new_client(self):
    #     # CREATE PART
    #     self.login_with_valid_user()
    #     self.add_client_details()
    #     self.white_labeling()
    #     self.property_portfolio()
    #     self.regions()
    #     self.lanlords()
    #     self.area_of_compliance()
    #     self.task_group()
    #     self.task_status()
    #     self.task_interval()
    #     self.action_status()
    #     self.task_repository()
    #     self.roles()
    #     self.cient_users()
    #     self.client_document_library()
    #     self.tasks()
    #     self.actions()
    #     self.supplier_business()
    #     self.supplier()
    #     self.email_notification_config()
    #     self.accident_category()
    #     self.finalization()
    #     # EDIT PART
    #     self.edit_accident_category()
    #     self.edit_email_notification_config()
    #     self.edit_supplier()
    #     self.edit_supplier_business()
    #     self.edit_actions()
    #     # self.edit_tasks()
    #     # self.client_users()
    #     # self.edit_roles()
    #     # self.edit_task_repository()
    #     # self.edit_action_status()
    #     # self.edit_task_interval()
    #     # self.edit_task_status()
    #     # self.edit_task_group()
    #     # self.edit_area_of_compliance()
    #     # self.edit_landlords()
    #     # self.edit_regions()
    #     # self.edit_property_portfolio()
    #     # # DELETE PART
    #     # self.del_property_portfolio()
    #     # self.del_region()
    #     # self.del_landlords()
    #     # self.del_area_of_compliance()
    #     # self.del_task_group()
    #     # self.del_task_status()
    #     # self.del_task_interval()
    #     # self.del_action_status()
    #     # self.del_task_repository()
    #     # self.del_roles()
    #     # self.del_client_users()
    #     # self.del_tasks()
    #     # self.del_actions()


    # def test_sign_in_with_invalid_user(self):
    #     print('\n' + str(test_cases(5)))
    #     mainPage = MainPage(self.browser)
    #     loginPage = mainPage.click_sign_in_button()
    #     result = loginPage.login_with_in_valid_user("invalid_user")
    #     self.assertIn("There was a problem with your request", result)

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    nose.run(defaultTest="", argv=TEST_PARAMS)
