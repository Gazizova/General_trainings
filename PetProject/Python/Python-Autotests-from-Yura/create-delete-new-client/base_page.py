import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import argparse
import logging
import sys
import datetime
import time
import random
import string
from functools import wraps
from edit_functions import EditFunctions
import nose
from random import randint

edit_instance = EditFunctions()

# Example for using:
# edit_instance.edit_random_digits()

__author__ = 'yuriy@strikersoft.com'
__description__ = "Tetra test"

DEFAULT_WEB_DRIVER = 'Chrome'
#DEFAULT_HOST = 'https://api.tetrapops.com'
DEFAULT_HOST = 'https://tetra-qa.strikersoft.com'
DEFAULT_PASSWORD = '12345+'
DEFAULT_EXECUTABLE = './chromedriver'
TEST_PARAMS = ['', __file__, '-v', '--all-modules', '--with-xunit', '--xunit-file=test_report.xml']

random_value = randint(10**(5-1), (10**5)-1)
# now = datetime.datetime.now().timestamp()
random_for_region = randint(10**(4-1), (10**4)-1)
random_value_lanlords = randint(10**(5-1), (10**5)-1)
random_new_lanlords = randint(10**(5-1), (10**5)-1)
random_area_of_compliance = randint(10**(4-1), (10**4)-1)
random_task_group = randint(10**(5-1), (10**5)-1)
random_code_task_status = randint(10**(5-1), (10**5)-1)
random_code_task_repository = randint(10**(5-1), (10**5)-1)
random_taskinterval_digits = randint(10**(2-1), (10**2)-1)
random_not_due_digits = randint(10**(2-1), (10**2)-1)
random_task_digits = randint(10**(5-1), (10**5)-1)
random_add_action = randint(10**(5-1), (10**5)-1)
random_new_supplier_business = randint(10**(5-1), (10**5)-1)
random_accident_category = randint(10**(5-1), (10**5)-1)


class TestMethods(unittest.TestCase):
    logging.basicConfig(stream=sys.stdout, level=logging.WARN,
                        format='%(asctime)s - '
                               '%(name)s - '
                               '%(levelname)s - '
                               '%(message)s')
    #
    # def __init__(self, test_name, **kwargs):
    #     super(TestMethods, self).__init__(test_name)
    #     parser = argparse.ArgumentParser(description=__description__)
    #     parser.add_argument('--host', required=False, help='Host address', default=DEFAULT_HOST)
    #     parser.add_argument('--user', required=False, help='User to use')
    #     parser.add_argument('--password', required=False, help='password to use', default=DEFAULT_PASSWORD)
    #     parser.add_argument('--webdriver', required=False, help='webdriver to use', default=DEFAULT_WEB_DRIVER)
    #     parser.add_argument(
    #         '--executable',
    #         required=False,
    #         help='webdriver executable, must match the webdriver',
    #         default=DEFAULT_EXECUTABLE
    #     )
    #     self.enviroment_args, unknown = parser.parse_known_args()

    def setUp(self):
        self.browser = getattr(
            webdriver, self.enviroment_args.webdriver.capitalize()
        )(executable_path=self.enviroment_args.executable)
        self.browser.implicitly_wait(5)
        self.browser.get('{}/operational/login.html'.format(self.enviroment_args.host))
        self.browser.maximize_window()

    def random_digits(self):
        return random_value

    def random_supplier_digits(self):
        return random_new_supplier_business

    def random_add_accident_category(self):
        return random_accident_category

    def random_digits_add_action(self):
        return random_add_action

    def random_not_due_yet_multiplier(self):
        return random_not_due_digits

    def task_interval_multiplier(self):
        return random_taskinterval_digits

    def random_digits_regions(self):
        return random_for_region

    def random_digits_for_lanlords(self):
        return random_value_lanlords

    def random_digits_new_lanlord(self):
        return random_new_lanlords

    def random_digits_area_of_compliance(self):
        return random_area_of_compliance

    def random_digits_task_group(self):
        return random_task_group

    def random_digits_task_status(self):
        return random_code_task_status

    def random_digits_new_repository(self):
        return random_code_task_repository

    def random_digits_task(self):
        return random_task_digits

    domains = ["hotmail.com", "gmail.com", "aol.com", "mail.kz", "yahoo.com"]
    letters = string.ascii_lowercase[:12]

    def get_random_domain(self, domains):
         return random.choice(domains)

    def get_random_name(self, letters, length):
         return ''.join(random.choice(letters) for i in range(length))

    def generate_random_emails(self, nb, length):
         return [self.get_random_name(self.letters, length) + '@' + self.get_random_domain(self.domains) for i in range(nb)]

    def main(self):
         return self.generate_random_emails(1, 7)[0]


    def login_with_valid_user(self):
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
        log_out_button = self.browser.find_element_by_xpath(
            '//*[@id="bs-example-navbar-collapse-6"]/p')
        self.assertEqual(log_out_button.text, 'Sign in as pops-admin')

    def add_client_details(self):
        client_management_1 = self.browser.find_element_by_xpath(
            '//*[@id="bs-example-navbar-collapse-6"]/ul/li[6]/a')
        client_management_1.click()
        add_new_client = self.browser.find_element_by_xpath(
            '//*[@id="bs-example-navbar-collapse-6"]/ul/li[6]/ul/li[1]/a')
        add_new_client.click()
        time.sleep(3)
        ref_num = self.browser.find_element_by_xpath(
            '//*[@id="clientCode"]')
        ref_num.send_keys(self.random_digits())
        name_field = self.browser.find_element_by_xpath(
            '//*[@id="clientName"]')
        name_field.send_keys('Client created by Python')
        property_name = self.browser.find_element_by_xpath(
            '//*[@id="record.address1"]')
        property_name.send_keys('Property name created by Python')
        street_1 = self.browser.find_element_by_xpath(
            '//*[@id="record.address2"]')
        street_1.send_keys('address created by Python')
        postcode = self.browser.find_element_by_xpath(
            '//*[@id="record.postCode"]')
        postcode.send_keys(self.random_digits())
        create_button = self.browser.find_element_by_id('submit')
        create_button.click()
        time.sleep(20)
        client_details = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[1]/a[2]')
        self.assertEqual(client_details.text, 'Client details')

    def add_file_white_labeling(self):
        self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[3]/div[2]/form/div[1]/div[1]/div/div/span/span/input').send_keys(
            '{}{}images.jpg'.format(os.getcwd(), os.sep))
        image_field = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[3]/div[2]/form/div[1]/div[2]/div/div/img')
        self.assertIn(image_field.text, 'images.jpg')

    def add_file_2_white_labeling(self):
        self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[3]/div[2]/form/div[1]/div[1]/div/div/span/span/input').send_keys(
            '{}{}image_2.jpg'.format(os.getcwd(), os.sep))
        image_field = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[3]/div[2]/form/div[1]/div[2]/div/div/img')
        self.assertIn(image_field.text, 'image_2.jpg')

    def add_favicon(self):
        self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[3]/div[2]/form/div[2]/div[1]/div/div/span/span/input').send_keys(
            '{}{}favicon.ico'.format(os.getcwd(), os.sep))
        favicon_field = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[3]/div[2]/form/div[2]/div[2]/div/div/img')
        self.assertIn(favicon_field.text, 'favicon.ico')

    def add_favicon_2(self):
        self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[3]/div[2]/form/div[2]/div[1]/div/div/span/span/input').send_keys(
            '{}{}favicon_2.ico'.format(os.getcwd(), os.sep))
        favicon_field = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[3]/div[2]/form/div[2]/div[2]/div/div/img')
        self.assertIn(favicon_field.text, 'favicon_2.ico')

    def white_labeling(self):
        white_labeling = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[2]/a[2]')
        white_labeling.click()
        self.add_file_white_labeling()
        self.add_favicon()
    def add_file_property_portfolio(self):
        self.browser.find_element_by_xpath(
            '//*[@id="browseLogo"]/input').send_keys(
            '{}{}images.jpg'.format(os.getcwd(), os.sep))
    def add_file_to_tasks(self):
        self.browser.find_element_by_xpath(
            '//*[@id="add-file"]').send_keys(
            '{}{}images.jpg'.format(os.getcwd(), os.sep))
    def add_file_company_library(self):
        self.browser.find_element_by_xpath(
            '//*[@id="add-file"]').send_keys(
            '{}{}images.jpg'.format(os.getcwd(), os.sep))

    def add_file_3d_report(self):
        self.browser.find_element_by_xpath(
            '//*[@id="model"]/div[5]/a').send_keys(
            '{}{}images.jpg'.format(os.getcwd(), os.sep))

    def _print_doc(self, doc, _type=None):
        if _type == 'warn':
            pass
        print('-' * len(doc) + '\n{}\n'.format(doc) + '-' * len(doc))

    def doc_print(func):
         @wraps(func)
         def wrapper(*args, **kw):
            doc = func.__doc__.strip()
            print('*' * len(doc) + '\n{}\n'.format(doc) + '*' * len(doc))
            try:
                res = func(*args, **kw)
            finally:
                pass
            return res

         return wrapper

    def assertTrue(self, expr, msg=None):
        doc = 'Check that something is return true. (Additional description: {})'.format(msg)
        self._print_doc(doc)
        return unittest.TestCase.assertTrue(self, expr, msg)

    def property_portfolio(self):
        property = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[4]/a[2]')
        property.click()
        time.sleep(5)
        tetra_ref_number = self.browser.find_element_by_id('record.code')
        tetra_ref_number.send_keys(self.random_digits())
        street_1 = self.browser.find_element_by_xpath(
            '//*[@id="record.address2"]')
        street_1.send_keys(self.random_digits())
        postcode = self.browser.find_element_by_xpath(
            '//*[@id="record.postCode"]')
        postcode.send_keys('12345')
        landlord_field = self.browser.find_element_by_xpath(
            '//*[@id="model"]/div[1]/div[2]/div[3]/div/span/input[2]')
        landlord_field.send_keys(self.random_digits_for_lanlords())
        region_field = self.browser.find_element_by_xpath(
            '//*[@id="model"]/div[1]/div[2]/div[4]/div/span/input[2]')
        region_field.send_keys(self.random_digits_regions())
        self.add_file_property_portfolio()
        create_button = self.browser.find_element_by_xpath(
            '//*[@id="submit"]')
        create_button.click()
        search_field = self.browser.find_element_by_xpath(
            '//*[@id="dict-table_filter"]/label/input')
        search_field.send_keys(self.random_digits())
        edit_button = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[7]/a[1]')
        edit_button.click()
        image_field = self.browser.find_element_by_xpath(
            '//*[@id="logos-list"]/div/div/img')
        self.assertIn(image_field.text, 'images.jpg')
        save = self.browser.find_element_by_xpath(
            '//*[@id="submit"]')
        save.click()
    def regions(self):
        regions = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[5]/a[2]')
        regions.click()
        search_field = self.browser.find_element_by_xpath(
            '//*[@id="dict-table_filter"]/label/input')
        search_field.send_keys(self.random_digits_regions())
        name_field = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[1]')
        # self.assertEqual(int(name_field.text), int(random_for_region))
        add_button = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/a')
        add_button.click()
        code_field = self.browser.find_element_by_xpath(
            '//*[@id="record.code"]')
        code_field.send_keys(self.random_digits())
        name_field = self.browser.find_element_by_xpath(
            '//*[@id="record.name"]')
        name_field.send_keys(self.random_digits_regions())
        create = self.browser.find_element_by_xpath(
            '//*[@id="submit"]')
        create.click()
        search_field = self.browser.find_element_by_xpath(
            '//*[@id="dict-table_filter"]/label/input')
        search_field.send_keys(self.random_digits_regions())
        # add assert
    def lanlords(self):
        lanlords = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[6]/a[2]')
        lanlords.click()
        search_lanlord = self.browser.find_element_by_xpath(
            '//*[@id="dict-table_filter"]/label/input')
        search_lanlord.send_keys(self.random_digits_for_lanlords())
        name_field_lanlord = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[1]')
        # self.assertEqual(int(name_field_lanlord.text), int(random_value_lanlords))
        add_lanlord = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/a')
        add_lanlord.click()
        landlord_code = self.browser.find_element_by_xpath(
            '//*[@id="record.code"]')
        landlord_code.send_keys(self.random_digits())
        name = self.browser.find_element_by_xpath(
            '//*[@id="record.name"]')
        name.send_keys(self.random_digits_new_lanlord())
        create = self.browser.find_element_by_xpath(
            '//*[@id="submit"]')
        create.click()
        search_lanlord = self.browser.find_element_by_xpath(
            '//*[@id="dict-table_filter"]/label/input')
        search_lanlord.send_keys(self.random_digits_new_lanlord())
        time.sleep(10)
        name_field_lanlord = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[1]')
        self.assertEqual(int(name_field_lanlord.text), int(random_new_lanlords))

    def area_of_compliance(self):
        area_of_compliance = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[7]/a[2]')
        area_of_compliance.click()
        add_button = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/a')
        add_button.click()
        code = self.browser.find_element_by_id(
            'record.code')
        code.send_keys(self.random_digits_area_of_compliance())
        name = self.browser.find_element_by_xpath(
            '//*[@id="record.name"]')
        name.send_keys(self.random_digits_area_of_compliance())
        create = self.browser.find_element_by_xpath('//*[@id="submit"]')
        create.click()
        search_area = self.browser.find_element_by_xpath(
            '//*[@id="dict-table_filter"]/label/input')
        search_area.send_keys(self.random_digits_area_of_compliance())
        name = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[2]')
        time.sleep(30)
        # self.assertEqual(int(name.text), int(random_area_of_compliance))

    def task_group(self):
        task_group = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[8]/a[2]')
        task_group.click()
        add = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/a')
        add.click()
        code = self.browser.find_element_by_xpath(
            '//*[@id="record.code"]')
        code.send_keys(self.random_digits())
        name_field = self.browser.find_element_by_xpath(
            '//*[@id="record.name"]')
        name_field.send_keys(self.random_digits_task_group())
        create = self.browser.find_element_by_xpath(
            '//*[@id="submit"]')
        create.click()
        time.sleep(10)
        name_in_list = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[1]')
        self.assertEqual(int(name_in_list.text), int(random_task_group))

    def task_status(self):
        task_status = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[9]/a[2]')
        task_status.click()
        # add new for Open
        add_open_task_status = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[4]/a')
        add_open_task_status.click()
        code = self.browser.find_element_by_id(
            'record.code')
        code.send_keys(self.random_digits())
        name = self.browser.find_element_by_xpath(
            '//*[@id="record.name"]')
        name.send_keys(self.random_digits_task_status())
        default = self.browser.find_element_by_xpath(
            '//*[@id="record.defaultDict1"]')
        default.click()
        create = self.browser.find_element_by_xpath(
            '//*[@id="submit"]')
        create.click()
        search_status = self.browser.find_element_by_xpath(
            '//*[@id="open-status_filter"]/label/input')
        search_status.send_keys(self.random_digits_task_status())
        time.sleep(5)
        open_task_status = self.browser.find_element_by_xpath(
            '//*[@id="open-status"]/tbody/tr[1]/td[1]')
        self.assertEqual(int(open_task_status.text), int(random_code_task_status))
        # add new Completed Task Status
        add_completed_task_status = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[6]/a')
        add_completed_task_status.click()
        code = self.browser.find_element_by_id(
            'record.code')
        code.send_keys(self.random_digits_task_status())
        name_completed_task_status = self.browser.find_element_by_id(
            'record.name')
        name_completed_task_status.send_keys(self.random_digits())
        default = self.browser.find_element_by_id('record.defaultDict1')
        default.click()
        create = self.browser.find_element_by_xpath(
            '//*[@id="submit"]')
        create.click()
        search = self.browser.find_element_by_xpath(
            '//*[@id="completed-status_filter"]/label/input')
        search.clear()
        search.send_keys(self.random_digits())
        time.sleep(5)
        completed_task_status = self.browser.find_element_by_xpath(
            '//*[@id="completed-status"]/tbody/tr/td[1]')
        self.assertEqual(int(completed_task_status.text), int(random_value))

    def task_interval(self):
        task_interval = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[10]/a[2]')
        task_interval.click()
        add = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/a')
        add.click()
        code = self.browser.find_element_by_id(
            'record.code')
        code.send_keys(self.random_digits())
        name_completed_task_status = self.browser.find_element_by_id(
            'record.name')
        name_completed_task_status.send_keys(self.random_digits())
        interval_multiplier = self.browser.find_element_by_id(
            'record.intervalValue')
        interval_multiplier.send_keys(self.task_interval_multiplier())
        not_due_yet_multiplier = self.browser.find_element_by_id(
            'record.upcomingValue')
        not_due_yet_multiplier.send_keys(
            self.random_not_due_yet_multiplier())
        create = self.browser.find_element_by_id('submit')
        create.click()
        name_field = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[1]')
        self.assertEqual(int(name_field.text), int(random_value))

    def action_status(self):
        action_status = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[11]/a[2]')
        action_status.click()
        # Open Action Status
        add = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[3]/a')
        add.click()
        code = self.browser.find_element_by_id(
            'record.code')
        code.send_keys(self.random_digits())
        name = self.browser.find_element_by_xpath(
            '//*[@id="record.name"]')
        name.send_keys(self.random_digits())
        default = self.browser.find_element_by_xpath(
            '//*[@id="record.defaultDict1"]')
        default.click()
        create = self.browser.find_element_by_xpath(
            '//*[@id="submit"]')
        create.click()
        search = self.browser.find_element_by_xpath(
            '//*[@id="open-status_filter"]/label/input')
        search.send_keys(self.random_digits())
        open_action_status = self.browser.find_element_by_xpath(
            '//*[@id="open-status"]/tbody/tr[1]/td[1]')
        self.assertEqual(int(open_action_status.text), int(random_value))

    def task_repository(self):
        task_repository = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[12]/a[2]')
        task_repository.click()
        add = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/a')
        add.click()
        code = self.browser.find_element_by_xpath(
            '//*[@id="record.code"]')
        code.send_keys(self.random_digits())
        name = self.browser.find_element_by_xpath(
            '//*[@id="record.name"]')
        name.send_keys(self.random_digits_new_repository())
        statutory = self.browser.find_element_by_xpath(
            '//*[@id="record.statutoryRequirement1"]')
        statutory.click()
        rd3_party_report = self.browser.find_element_by_xpath(
            '//*[@id="record.inspection1"]')
        rd3_party_report.click()
        file_required = self.browser.find_element_by_xpath(
            '//*[@id="record.fileRequired1"]')
        file_required.click()
        create = self.browser.find_element_by_xpath(
            '//*[@id="submit"]')
        create.click()
        name_field = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[1]')
        self.assertEqual(int(name_field.text), int(random_code_task_repository))

    def roles(self):
        roles = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[13]/a[2]')
        roles.click()
        add = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/a')
        add.click()
        code = self.browser.find_element_by_id('record.code')
        code.send_keys(self.random_digits())
        name = self.browser.find_element_by_id('record.name')
        name.send_keys(self.random_digits())
        general = self.browser.find_element_by_xpath(
            '//*[@id="model"]/div[2]/div/div/div[1]/div[1]/div[1]/label/input')
        general.click()
        menu = self.browser.find_element_by_xpath(
            '//*[@id="model"]/div[2]/div/div/div[1]/div[2]/div[1]/label/input')
        menu.click()
        elem = self.browser.find_element_by_tag_name('a')
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(5)
        supplier_details = self.browser.find_element_by_xpath(
             '//*[@id="model"]/div[2]/div/div/div[2]/div[5]/div[1]/label/input')
        supplier_details.click()
        reports = self.browser.find_element_by_xpath(
             '//*[@id="model"]/div[2]/div/div/div[2]/div[6]/div[1]/label/input')
        reports.click()
        create = self.browser.find_element_by_xpath(
            '//*[@id="submit"]')
        create.click()
        roles = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[13]/a[2]')
        roles.click()
        time.sleep(5)
        search = self.browser.find_element_by_xpath(
            '//*[@id="dict-table_filter"]/label/input')
        search.send_keys(self.random_digits())
        name = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr[1]/td[1]')
        self.assertEqual(int(name.text), int(random_value))

    def cient_users(self):
        client_users = self.browser.find_element_by_id('step_14')
        client_users.click()
        add = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/a')
        add.click()
        active = self.browser.find_element_by_id(
            'record.enabled1')
        active.click()
        full_name = self.browser.find_element_by_xpath(
            '//*[@id="record.fullName"]')
        full_name.send_keys(self.random_digits())
        email = self.browser.find_element_by_xpath(
            '//*[@id="record.login"]')
        email.send_keys(self.main())
        password = self.browser.find_element_by_xpath(
            '//*[@id="newPassword"]')
        password.send_keys('Password7/')
        confirm_password = self.browser.find_element_by_xpath(
            '//*[@id="newPasswordConfirm"]')
        confirm_password.send_keys('Password7/')
        add_property = self.browser.find_element_by_xpath(
            '//*[@id="prismUserRolesWidget"]/div/button')
        add_property.click()
        add = self.browser.find_element_by_xpath(
            '//*[@id="submit"]')
        add.click()
        save = self.browser.find_element_by_xpath(
            '//*[@id="submit"]')
        save.click()
        name_field = self.browser.find_element_by_xpath(
            '//*[@id="users-table"]/tbody/tr[1]/td[1]')
        self.assertEqual(int(name_field.text), int(random_value))

    def client_document_library(self):
        library = self.browser.find_element_by_id('step_15')
        library.click()
        add_folder = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[4]/div[3]/a[1]')
        add_folder.click()
        folder_name = self.browser.find_element_by_xpath(
            '//*[@id="folder-name"]')
        folder_name.send_keys(self.random_digits())
        time.sleep(10)
        add = self.browser.find_element_by_xpath(
            '//*[@id="create"]/div[2]/button[1]')
        add.click()
        time.sleep(5)
        add_file = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[4]/div[3]/a[2]')
        add_file.click()
        self.add_file_company_library()
        time.sleep(10)
        add_button = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div/div[3]/button[1]')
        add_button.click()
        time.sleep(5)

    def tasks(self):
        tasks = self.browser.find_element_by_id('step_16')
        tasks.click()
        # self.browser.get(
        #     'https://tetra-qa.strikersoft.com/operational/dictTask/list.html?clientId=894')
        time.sleep(5)
        add = self.browser.find_element_by_xpath(
            '//*[@id="model"]/a')
        add.click()
        property = self.browser.find_element_by_id(
            'record.propertyBriefInfo.id')
        property.click()
        property_value = self.browser.find_element_by_xpath(
            '//*[@id="record.propertyBriefInfo.id"]/option[2]')
        property_value.click()
        code = self.browser.find_element_by_id('record.code')
        code.send_keys(self.random_digits())
        name = self.browser.find_element_by_id('record.name')
        name.send_keys(self.random_digits_task())
        area_of_compliance = self.browser.find_element_by_xpath(
            '//*[@id="s2id_record.areaOfObservationIds"]/ul')
        area_of_compliance.click()
        environment = self.browser.find_element_by_xpath(
            '//*[@id="select2-result-label-3"]')
        environment.click()
        statutory = self.browser.find_element_by_id(
            'record.statutory1')
        statutory.click()
        rd3_party_report = self.browser.find_element_by_id(
            'record.inspection1')
        rd3_party_report.click()
        file_required = self.browser.find_element_by_id(
            'record.needFileCheck1')
        file_required.click()
        start_date = self.browser.find_element_by_id('record.start')
        start_date.clear()
        start_date.send_keys('11122016')
        start_date.submit()
        due_date = self.browser.find_element_by_id('record.due')
        due_date.clear()
        due_date.send_keys('11042017')
        due_date.submit()
        complete_date = self.browser.find_element_by_id('record.completion')
        complete_date.clear()
        complete_date.send_keys('11032017')
        complete_date.submit()
        create = self.browser.find_element_by_id('submit')
        create.click()
        time.sleep(5)
        # self.add_file_to_tasks()
        # time.sleep(5)
        # field_images = self.browser.find_element_by_xpath(
        #     '//*[@id="files-table"]/tbody/tr/td[1]/a')
        # self.assertEqual(field_images.text, 'images.jpg')
        add_action = self.browser.find_element_by_xpath(
            '//*[@id="model"]/a[3]')
        add_action.click()
        ref_num = self.browser.find_element_by_id('record.code')
        ref_num.send_keys(self.random_digits_task())
        action = self.browser.find_element_by_id('record.name')
        action.send_keys(self.random_digits_add_action())
        create = self.browser.find_element_by_id('submit')
        create.click()
        time.sleep(5)
        action_column = self.browser.find_element_by_xpath(
            '//*[@id="actions-table"]/tbody/tr[1]/td[2]')
        self.assertEqual(int(action_column.text), int(random_add_action))
        elem = self.browser.find_element_by_tag_name('a')
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(5)
        add_3rd_party_report = self.browser.find_element_by_xpath(
            '//*[@id="model"]/a[5]')
        add_3rd_party_report.click()
        ref_number = self.browser.find_element_by_id('record.ref')
        ref_number.send_keys(self.random_digits())
        company = self.browser.find_element_by_id('record.company')
        company.send_keys('Lucas test company')
        create = self.browser.find_element_by_xpath('//*[@id="submit"]')
        create.click()

    def actions(self):
        actions = self.browser.find_element_by_id(
            'step_17')
        actions.click()
        add = self.browser.find_element_by_xpath(
            '//*[@id="model"]/a')
        add.click()
        property = self.browser.find_element_by_id('record.propertyId')
        property.click()
        select_property = self.browser.find_element_by_xpath(
            '//*[@id="record.propertyId"]/option[2]')
        select_property.click()
        ref_num = self.browser.find_element_by_id('record.code')
        ref_num.send_keys(self.random_digits())
        action_field = self.browser.find_element_by_id('record.name')
        action_field.send_keys('Action created by Python')
        task = self.browser.find_element_by_id('record.taskId')
        task.click()
        select_task = self.browser.find_element_by_xpath(
            '//*[@id="record.taskId"]/option[2]')
        select_task.click()
        create = self.browser.find_element_by_xpath(
            '//*[@id="submit"]')
        create.click()
        save = self.browser.find_element_by_xpath(
            '//*[@id="submit"]')
        save.click()

    def supplier_business(self):
        supplier_business = self.browser.find_element_by_id(
            'step_18')
        supplier_business.click()
        add_button_s = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/a')
        add_button_s.click()
        code = self.browser.find_element_by_id('record.code')
        code.send_keys(self.random_digits())
        name = self.browser.find_element_by_id('record.name')
        name.send_keys(self.random_supplier_digits())
        create = self.browser.find_element_by_id('submit')
        create.click()
        search = self.browser.find_element_by_xpath(
            '//*[@id="dict-table_filter"]/label/input')
        search.send_keys(self.random_supplier_digits())
        name_field = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr[1]/td[1]')
        self.assertEqual(int(name_field.text), int(random_new_supplier_business))

    def supplier(self):
        supplier = self.browser.find_element_by_id(
            'step_19')
        supplier.click()
        add = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/a')
        add.click()
        company_name = self.browser.find_element_by_id('record.name')
        company_name.send_keys(self.random_supplier_digits())
        create = self.browser.find_element_by_id('submit')
        create.click()
        name_field_company = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[1]')
        self.assertEqual(int(name_field_company.text), int(random_new_supplier_business))

    def email_notification_config(self):
        email_notification_config = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[20]/a[2]')
        email_notification_config.click()
        add = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/a')
        add.click()
        code = self.browser.find_element_by_id('record.code')
        code.send_keys(self.random_digits())
        name = self.browser.find_element_by_id('record.name')
        name.send_keys(self.random_digits_task())
        permissions_needed = self.browser.find_element_by_xpath(
            '//*[@id="model"]/div/div/div[9]/div/span/span[1]/span/ul')
        permissions_needed.click()
        permissions_needed.submit()
        select = self.browser.find_element_by_id(
             'select2-record.requiredRoles-results')
        select.click()
        create = self.browser.find_element_by_id('submit')
        create.click()
        search_field = self.browser.find_element_by_xpath(
            '//*[@id="dict-table_filter"]/label/input')
        search_field.send_keys(self.random_digits_task())
        time.sleep(5)
        name_field = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[1]')
        self.assertEqual(int(name_field.text), int(random_task_digits))

    def accident_category(self):
        accident_category = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[21]/a[2]')
        accident_category.click()
        add = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/a')
        add.click()
        code = self.browser.find_element_by_id(
            'record.code')
        code.send_keys(self.random_digits())
        name = self.browser.find_element_by_id('record.name')
        name.send_keys(self.random_add_accident_category())
        riddor = self.browser.find_element_by_id('record.riddor1')
        riddor.click()
        create = self.browser.find_element_by_id('submit')
        create.click()
        name = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[1]')
        self.assertEqual(int(name.text), int(random_accident_category))
        simbol = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[3]/i')
        self.assertTrue(simbol.is_displayed(), msg='Riddor is active')

    def finalization(self):
        finalization = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[22]/a[2]')
        finalization.click()
        activate = self.browser.find_element_by_xpath(
            '//*[@id="submit"]')
        activate.click()
        # self.assertEqual(activate.text, 'Deactivate')

    def edit_accident_category(self):
        accident_category = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[21]/a[2]')
        accident_category.click()
        search_field = self.browser.find_element_by_xpath(
            '//*[@id="dict-table_filter"]/label/input')
        search_field.send_keys(self.random_add_accident_category())
        edit = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr[1]/td[4]/a[1]')
        edit.click()
        name = self.browser.find_element_by_id('record.name')
        name.clear()
        name.send_keys(edit_instance.edit_random_add_accident_category())
        save = self.browser.find_element_by_id('submit')
        save.click()
        name = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[1]')
        self.assertEqual(int(name.text),
                         int(edit_instance.get_edit_random_add_accident_category()))

    def edit_email_notification_config(self):
        email_notification_config = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[20]/a[2]')
        email_notification_config.click()
        edit = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[8]/a[1]')
        edit.click()
        name = self.browser.find_element_by_id('record.name')
        name.clear()
        name.send_keys(edit_instance.edit_email_notification_config())
        permissions_needed = self.browser.find_element_by_xpath(
            '//*[@id="model"]/div/div/div[9]/div/span/span[1]/span/ul')
        permissions_needed.click()
        permissions_needed.submit()
        # select = self.browser.find_element_by_id(
        #      'select2-record.requiredRoles-results')
        # select.click()
        # save = self.browser.find_element_by_id('submit')
        # save.click()
        search = self.browser.find_element_by_xpath(
            '//*[@id="dict-table_filter"]/label/input')
        search.clear()
        search.send_keys(edit_instance.edit_email_notification_config())
        time.sleep(5)
        name = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[1]')
        self.assertEqual(int(name.text),
                         int(edit_instance.get_edit_email_notification_config()))

    def edit_supplier(self):
        supplier = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[19]/a[2]')
        supplier.click()
        edit = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[8]/a[1]')
        edit.click()
        company_name = self.browser.find_element_by_id('record.name')
        company_name.clear()
        company_name.send_keys(edit_instance.edit_random_supplier_digits())
        save = self.browser.find_element_by_id('submit')
        save.click()
        name_field_company = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[1]')
        self.assertEqual(int(name_field_company.text),
                         int(edit_instance.get_edit_random_supplier_digits()))

    def edit_supplier_business(self):
        supplier_business = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[18]/a[2]')
        supplier_business.click()
        edit = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[3]/a[1]')
        edit.click()
        name = self.browser.find_element_by_id('record.name')
        name.clear()
        name.send_keys(edit_instance.edit_random_supplier_business())
        save = self.browser.find_element_by_id('submit')
        save.click()
        name_field = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[1]') # edit_random_supplier
        self.assertEqual(int(name_field.text),
                         int(edit_instance.get_random_supplier()))
    def edit_actions(self):
        actions = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[17]/a[2]')
        actions.click()
        edit = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr[1]/td[6]/a[1]')
        edit.click()
        action_required = self.browser.find_element_by_id('record.name')
        action_required.clear()
        action_required.send_keys(edit_instance.edit_random_digits_add_action())
        save = self.browser.find_element_by_id('submit')
        save.click()
        actions = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[17]/a[2]')
        actions.click()
        description = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[2]')
        self.assertEqual(int(description.text),
                         int(edit_instance.get_edit_random_digits_add_action()))
    def edit_tasks(self):
        tasks = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[16]/a[2]')
        tasks.click()
        edit = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[7]/a[1]')
        edit.click()
        name = self.browser.find_element_by_id('record.name')
        name.clear()
        name.send_keys(edit_instance.edit_random_digits_task())
        save = self.browser.find_element_by_id('submit')
        save.click()
        tasks = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[16]/a[2]')
        tasks.click()
        name = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[1]')
        self.assertEqual(int(name.text),
                         int(edit_instance.get_edit_random_digits_task()))

    def edit_client_users(self):
        client_users = self.browser.find_element_by_id('step_14')
        client_users.click()
        time.sleep(5)
        edit_button = self.browser.find_element_by_xpath(
            '//*[@id="users-table"]/tbody/tr/td[6]/a[1]')
        edit_button.click()
        full_name = self.browser.find_element_by_id(
            'record.fullName')
        full_name.clear()
        full_name.send_keys(edit_instance.edit_random_client_users())
        save = self.browser.find_element_by_id('submit')
        save.click()
        time.sleep(5)
        search_field = self.browser.find_element_by_xpath(
            '//*[@id="users-table_filter"]/label/input')
        search_field.send_keys(edit_instance.edit_random_client_users())
        name_field = self.browser.find_element_by_xpath(
            '//*[@id="users-table"]/tbody/tr[1]/td[1]')
        self.assertEqual(int(name_field.text),
                         int(edit_instance.get_edit_random_client_users()))

    def edit_roles(self):
        roles = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[13]/a[2]')
        roles.click()
        edit = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[3]/a[1]')
        edit.click()
        name = self.browser.find_element_by_id('record.name')
        name.clear()
        name.send_keys(edit_instance.edit_roles_digits())
        elem = self.browser.find_element_by_tag_name('a')
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(5)
        save = self.browser.find_element_by_id('submit')
        save.click()
        roles = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[13]/a[2]')
        roles.click()
        name = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr[1]/td[1]')
        self.assertEqual(int(name.text),
                         int(edit_instance.get_edit_roles_digits()))

    def edit_task_repository(self):
        task_repository = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[12]/a[2]')
        task_repository.click()
        edit = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[6]/a[1]')
        edit.click()
        name = self.browser.find_element_by_xpath(
            '//*[@id="record.name"]')
        name.clear()
        name.send_keys(edit_instance.edit_random_digits_new_repository())
        save = self.browser.find_element_by_id('submit')
        save.click()
        name = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[1]')
        self.assertEqual(int(name.text),
                         int(edit_instance.get_edit_random_digits_new_repository()))

    def edit_action_status(self):
        action_status = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[11]/a[2]')
        action_status.click()
        edit = self.browser.find_element_by_xpath(
            '//*[@id="open-status"]/tbody/tr/td[4]/a[1]')
        edit.click()
        name = self.browser.find_element_by_id('record.name')
        name.clear()
        name.send_keys(edit_instance.random_edit_action_status())
        save = self.browser.find_element_by_id('submit')
        save.click()
        search_field = self.browser.find_element_by_xpath(
            '//*[@id="open-status_filter"]/label/input')
        search_field.send_keys(edit_instance.random_edit_action_status())
        name = self.browser.find_element_by_xpath(
            '//*[@id="open-status"]/tbody/tr/td[1]')
        self.assertEqual(int(name.text), int(edit_instance.get_random_edit_action_status()))

    def edit_task_interval(self):
        task_interval = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[10]/a[2]')
        task_interval.click()
        edit = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[7]/a[1]')
        edit.click()
        name = self.browser.find_element_by_id(
            'record.name')
        name.clear()
        name.send_keys(edit_instance.edit_random_digits_task_status())
        save = self.browser.find_element_by_id('submit')
        save.click()
        name_field = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[1]')
        self.assertEqual(int(name_field.text),
                         int(edit_instance.get_edit_random_digits_task_status()))

    def edit_task_status(self):
        task_status = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[9]/a[2]')
        task_status.click()
        edit = self.browser.find_element_by_xpath(
            '//*[@id="completed-status"]/tbody/tr/td[4]/a[1]')
        edit.click()
        name = self.browser.find_element_by_xpath(
            '//*[@id="record.name"]')
        name.clear()
        name.send_keys(edit_instance.edit_random_digits_task_status())
        save = self.browser.find_element_by_id('submit')
        save.click()
        name_field = self.browser.find_element_by_xpath(
            '//*[@id="completed-status"]/tbody/tr/td[1]')
        # self.assertEqual(int(name_field.text),
        #                  int(edit_instance.get_edit_random_digits_task_status()))

    def edit_task_group(self):
        task_group = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[8]/a[2]')
        task_group.click()
        edit = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[3]/a[1]')
        edit.click()
        name_field = self.browser.find_element_by_xpath(
            '//*[@id="record.name"]')
        name_field.clear()
        name_field.send_keys(edit_instance.edit_random_digits_task_group())
        save = self.browser.find_element_by_id('submit')
        save.click()
        time.sleep(5)
        name_in_list = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[1]')
        self.assertEqual(int(name_in_list.text),
                         int(edit_instance.get_edit_random_digits_task_group()))

    def edit_area_of_compliance(self):
        area_of_compliance = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[7]/a[2]')
        area_of_compliance.click()
        edit = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr[1]/td[4]/a[1]')
        edit.click()
        name = self.browser.find_element_by_xpath(
            '//*[@id="record.name"]')
        name.clear()
        name.send_keys(edit_instance.edit_random_digits_area_of_compliance())
        save = self.browser.find_element_by_id('submit')
        save.click()

        search_area = self.browser.find_element_by_xpath('//*[@id="dict-table_filter"]/label/input')
        search_area.send_keys(edit_instance.edit_random_digits_area_of_compliance())
        name = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[2]')
        self.assertEqual(int(name.text),
                         int(edit_instance.get_edit_random_digits_area_of_compliance()))

    def edit_landlords(self):
        lanlords = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[6]/a[2]')
        lanlords.click()
        edit = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[4]/a[1]')
        edit.click()
        name = self.browser.find_element_by_xpath(
            '//*[@id="record.name"]')
        name.clear()
        name.send_keys(edit_instance.edit_random_digits_for_lanlords())
        save = self.browser.find_element_by_id('submit')
        save.click()
        search_lanlord = self.browser.find_element_by_xpath(
            '//*[@id="dict-table_filter"]/label/input')
        search_lanlord.clear()
        search_lanlord.send_keys(edit_instance.edit_random_digits_for_lanlords())
        time.sleep(5)
        name_field_lanlord = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[1]')
        self.assertEqual(int(name_field_lanlord.text),
                         int(edit_instance.get_edit_random_digits_for_lanlords()))

    def edit_regions(self):
        regions = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[5]/a[2]')
        regions.click()
        edit = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[4]/a[1]')
        edit.click()
        name = self.browser.find_element_by_xpath(
            '//*[@id="record.name"]')
        name.clear()
        name.send_keys(edit_instance.edit_random_digits_regions())
        save = self.browser.find_element_by_id('submit')
        save.click()
        search = self.browser.find_element_by_xpath(
            '//*[@id="dict-table_filter"]/label/input')
        search.send_keys(edit_instance.edit_random_digits_regions())
        time.sleep(5)
        name_field = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[1]')
        self.assertEqual(int(name_field.text),
                         int(edit_instance.get_edit_random_digits_regions()))

    def edit_property_portfolio(self):
        property = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[4]/a[2]')
        property.click()
        edit = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[7]/a[1]')
        edit.click()
        street_address = self.browser.find_element_by_xpath(
            '//*[@id="record.address2"]')
        street_address.clear()
        street_address.send_keys(edit_instance.edit_edit_property_portfolio())
        save = self.browser.find_element_by_id('submit')
        save.click()
        address_field = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[1]')
        self.assertEqual(int(address_field.text),
                         int(edit_instance.get_edit_edit_property_portfolio()))

         # DELETE PART

    def del_property_portfolio(self):
        deactivate = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[7]/a[2]')
        deactivate.click()
        time.sleep(3)
        alert = self.browser.switch_to_alert()
        alert.accept()
        deactivate = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[7]/a[2]')
        self.assertIn(deactivate.text, 'Activate')

    def del_region(self):
        regions = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[5]/a[2]')
        regions.click()
        delete = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr[1]/td[4]/a[2]')
        delete.click()
        alert = self.browser.switch_to_alert()
        alert.accept()
        warning = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[3]')
        self.assertIn(warning.text,
                         "Can't delete entity because it has relations with other entities.")

    def del_landlords(self):
        lanlords = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[6]/a[2]')
        lanlords.click()
        delete = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr[1]/td[4]/a[2]')
        delete.click()
        alert = self.browser.switch_to_alert()
        alert.accept()
        warning = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[3]')
        self.assertNotIn(warning.text,
                         "Can't delete entity because it has relations with other entities.")

    def del_area_of_compliance(self):
        area_of_compliance = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[7]/a[2]')
        area_of_compliance.click()
        delete = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr[1]/td[4]/a[2]')
        delete.click()
        alert = self.browser.switch_to_alert()
        alert.accept()
        warning = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[3]')
        self.assertIn(warning.text,
                         "Can't delete entity because it has relations with other entities.")

    def del_task_group(self):
        task_group = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[8]/a[2]')
        task_group.click()
        delete = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[3]/a[2]')
        delete.click()
        alert = self.browser.switch_to_alert()
        alert.accept()
        warning = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[3]')
        self.assertIn(warning.text,
                         "Can't delete entity because it has relations with other entities.")

    def del_task_status(self):
        task_status = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[9]/a[2]')
        task_status.click()
        delete = self.browser.find_element_by_xpath(
            '//*[@id="completed-status"]/tbody/tr/td[4]/a[2]')
        delete.click()
        alert = self.browser.switch_to_alert()
        alert.accept()
        task_status = self.browser.find_element_by_xpath(
            '//*[@id="completed-status"]/tbody/tr/td')
        self.assertIn(task_status.text, 'No data available in table')

    def del_task_interval(self):
        task_interval = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[10]/a[2]')
        task_interval.click()
        delete = self.browser.find_element_by_xpath(
           '//*[@id="dict-table"]/tbody/tr/td[7]/a[2]')
        delete.click()
        alert = self.browser.switch_to_alert()
        alert.accept()
        warning = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[3]')
        self.assertIn(warning.text,
                      "Can't delete entity because it has relations with other entities.")

    def del_action_status(self):
        action_status = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[11]/a[2]')
        action_status.click()
        delete = self.browser.find_element_by_xpath(
            '//*[@id="open-status"]/tbody/tr/td[4]/a[2]')
        delete.click()
        alert = self.browser.switch_to_alert()
        alert.accept()
        warning = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[3]')
        self.assertEqual(warning.text,
                         "Can't delete entity because it has relations with other entities.")

    def del_task_repository(self):
        task_repository = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[12]/a[2]')
        task_repository.click()
        delete = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[6]/a[2]')
        delete.click()
        alert = self.browser.switch_to_alert()
        alert.accept()
        warning = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[3]')
        self.assertNotIn(warning.text,
                         "Can't delete entity because it has relations with other entities.")

    def del_roles(self):
        roles = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[13]/a[2]')
        roles.click()
        delete = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[3]/a[2]')
        delete.click()
        alert = self.browser.switch_to_alert()
        alert.accept()
        warning = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[3]')
        self.assertNotIn(warning.text,
                         "Can't delete entity because it has relations with other entities.")

    def del_client_users(self):
        client_users = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[14]/a[2]')
        client_users.click()
        delete = self.browser.find_element_by_xpath(
            '//*[@id="users-table"]/tbody/tr/td[5]/a[2]')
        delete.click()
        alert = self.browser.switch_to_alert()
        alert.accept()
        full_name = self.browser.find_element_by_xpath(
            '//*[@id="users-table"]/tbody/tr/td')
        self.assertIn(full_name.text, 'No data available in table')

    # need to Clarify!!!
    # def del_client_document_library(self):

    def del_tasks(self):
        self.browser.get(
            'https://tetra-qa.strikersoft.com/operational/dictTask/list.html?clientId=224')
        delete = self.browser.find_element_by_xpath(
            '//*[@id="dict-table"]/tbody/tr/td[7]/a[2]')
        delete.click()
        alert = self.browser.switch_to_alert()
        alert.accept()
        warning = self.browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[3]')
        self.assertIn(warning.text,
                         "Can't delete entity because it has relations with other entities.")

    # def del_actions(self):
    #     actions = self.browser.find_element_by_xpath(
    #         '/html/body/div[2]/div/div[1]/ul/li[17]/a[2]')
    #     actions.click()
    #     delete = self.browser.find_element_by_xpath(
    #         '//*[@id="dict-table"]/tbody/tr[1]/td[6]/a[2]')
    #     delete.click()
    #     alert = self.browser.switch_to_alert()
    #     alert.accept()
    #     count_items = self.browser.find_element_by_xpath(
    #         '//*[@id="dict-table_info"]')
    #     self.assertEqual(count_items.text, 'Showing 1 to 1 of 1 entries')
    #     sorting_button = self.browser.find_element_by_xpath(
    #         '//*[@id="dict-table"]/tbody/tr[1]/td[1]')
    #     sorting_button.click()
    #     delete = self.browser.find_element_by_xpath(
    #         '//*[@id="dict-table"]/tbody/tr[2]/td/ul/li[4]/span[2]/a[2]')
    #     delete.click()
    #     alert = self.browser.switch_to_alert()
    #     alert.accept()
    #     property = self.browser.find_element_by_xpath(
    #         '//*[@id="dict-table"]/tbody/tr/td')
    #     self.assertEqual(property.text, 'No data available in table')

if __name__ == '__main__':
    nose.run(defaultTest="", argv=TEST_PARAMS)




