import unittest
from selenium import webdriver
from random import randint
from selenium.webdriver.support.ui import Select
import datetime
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from methods import TestMethods
import nose
import argparse #NTC
import logging
import sys

__author__ = 'yuriy@strikersoft.com'
__description__ = "Tetra test"

DEFAULT_WEB_DRIVER = 'Chrome'
#DEFAULT_HOST = 'https://api.tetrapops.com'
DEFAULT_HOST = 'https://tetra-dev.strikersoft.com'
DEFAULT_PASSWORD = '12345+'
DEFAULT_EXECUTABLE = './chromedriver.exe'

TEST_PARAMS = ['', __file__, '-v', '--all-modules', '--with-xunit', '--xunit-file=test_report.xml'] # what is it?

random_value = randint(10**(5-1), (10**5)-1) # NTC
now = datetime.datetime.now().timestamp()
# Is it all - definitions for other work?

class TestTypical(TestMethods):
        " Project stages tests for tetra"
        logging.basicConfig(stream=sys.stdout, level=logging.WARN, # NTC
                            format='%(asctime)s - '
                                   '%(name)s - '
                                   '%(levelname)s - '
                                   '%(message)s')

        def __init__(self, test_name, **kwargs): #NTC - where is login?
            super(TestTypical, self).__init__(test_name)
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

        def setUp(self): #NTC
            self.browser = getattr(
                webdriver, self.enviroment_args.webdriver.capitalize()
            )(executable_path=self.enviroment_args.executable)
            self.browser.implicitly_wait(5)
            self.browser.get('{}/operational/login.html'.format(self.enviroment_args.host))
            self.browser.maximize_window()

        def random_digits(self):
            return random_value


        def test_a(self):
            self.login_as_operator()
            project_tool = self.browser.find_element_by_xpath( #check project_tool
                '//*[@id="bs-example-navbar-collapse-6"]/ul/li[2]/a')
            project_tool.click()
            create_project = self.browser.find_element_by_xpath( #Create Project
                '//*[@id="bs-example-navbar-collapse-6"]/ul/li[2]/ul/li/a')
            create_project.click()
            ref_num = self.browser.find_element_by_id('record.code') #input Project Ref Number
            ref_num.send_keys(self.random_digits())
            code = self.browser.find_element_by_id('record.property.code')#input Project code
            code.send_keys(self.random_digits())
            property_name = self.browser.find_element_by_id( #input property name
                'record.property.address1')
            property_name.send_keys(
                'Test property name')
            client_name = self.browser.find_element_by_id( #input client name
                'record.property.clientName')
            client_name.send_keys('Test client name')
            contact = self.browser.find_element_by_id(
                'record.propertyContactDto.name')
            contact.send_keys('Test contact')
            add_button = self.browser.find_element_by_xpath(
                '//*[@id="actionAdd"]')
            add_button.click()
            project_stage = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertIn(project_stage.text, 'JSS')
            assign_consultant = self.browser.find_element_by_xpath(
                '//*[@id="assignee-actions"]/div')
            assign_consultant.click()
            assign_2_element = self.browser.find_element_by_xpath(
                '//*[@id="actionsAssignee"]')
            assign_2_element.click()
            consultant_1 = Select(self.browser.find_element_by_xpath(
                '//*[@id="actionsAssignee"]'))
            consultant_1.select_by_visible_text('consultant1')
            allocate = self.browser.find_element_by_id(
                'actionStage_ASSIGNED_TO_CONSULTANT')
            allocate.click()
            project_stage = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertIn(project_stage.text,
                          'Assigned to consultant')

        def test_b_2(self):
            self.login_as_consultant_1()
            ref_num_search = self.browser.find_element_by_xpath(
                '//*[@id="refNum"]')
            ref_num_search.send_keys(self.random_digits())
            search_button = self.browser.find_element_by_xpath(
                '//*[@id="downloadProjects-form"]/div/div[1]/div[2]/div[3]/div/button')
            search_button.click()
            time.sleep(5)
            stage_status = self.browser.find_element_by_xpath(
                '//*[@id="tasks-table"]/tbody/tr/td[6]')
            self.assertIn(stage_status.text, 'Assigned to consultant')
            project_link = self.browser.find_element_by_xpath(
                '//*[@id="tasks-table"]/tbody/tr/td[7]/a')
            project_link.click()
            project_status_field = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertEqual(project_status_field.text, 'Assigned to consultant')
            return_to_operator = self.browser.find_element_by_xpath(
                '//*[@id="actionreturnToOperator"]')
            return_to_operator.click()
            alert = self.browser.find_element_by_xpath(
                '//*[@id="parsley-id-6"]/li')
            self.assertIn(alert.text,
                          'This value is required.')
            comment_field = self.browser.find_element_by_xpath(
                '//*[@id="record.comment"]')
            comment_field.send_keys('comment from Python')
            return_to_operator.click()
            wait = WebDriverWait(self.browser, 10)
            jss_status = wait.until(EC.visibility_of_element_located((By.XPATH,
                    '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')))
            self.assertIn(jss_status.text, 'JSS')

        def test_c_3(self):
            self.login_as_operator()
            ref_num_search = self.browser.find_element_by_xpath(
                '//*[@id="refNum"]')
            ref_num_search.send_keys(self.random_digits())
            search_button = self.browser.find_element_by_xpath(
                '//*[@id="downloadProjects-form"]/div/div[1]/div[2]/div[3]/div/button')
            search_button.click()
            time.sleep(5)
            project_link = self.browser.find_element_by_xpath(
                '//*[@id="tasks-table"]/tbody/tr/td[7]/a')
            project_link.click()
            wait = WebDriverWait(self.browser, 5)
            jss_status = wait.until(EC.visibility_of_element_located\
                                        ((By.XPATH, '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')))
            self.assertEqual(jss_status.text, 'JSS')
            # ASSERT FOR COMMENTS
            comment_field = self.browser.find_element_by_xpath(
                 '//*[@id="record.comment"]')
            # self.assertEqual(comment_field.text, 'comment from Python')
            # Assign consultant
            assign_consultant = self.browser.find_element_by_xpath(
                '//*[@id="assignee-actions"]/div')
            assign_consultant.click()
            assign_2_element = self.browser.find_element_by_xpath(
                '//*[@id="actionsAssignee"]')
            assign_2_element.click()
            consultant_1 = Select(self.browser.find_element_by_xpath(
                '//*[@id="actionsAssignee"]'))
            consultant_1.select_by_visible_text('consultant1')
            allocate = self.browser.find_element_by_id(
                'actionStage_ASSIGNED_TO_CONSULTANT')
            allocate.click()
            time.sleep(5)
            project_stage = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertEqual(project_stage.text,
                          'Assigned to consultant')

        def test_d_4(self):
            self.login_as_consultant_1()
            ref_num_search = self.browser.find_element_by_xpath(
                '//*[@id="refNum"]')
            ref_num_search.send_keys(self.random_digits())
            search_button = self.browser.find_element_by_xpath(
                '//*[@id="downloadProjects-form"]/div/div[1]/div[2]/div[3]/div/button')
            check_box = self.browser.find_element_by_xpath('//*[@id="myTasks1"]')
            check_box.click()
            search_button.click()
            time.sleep(5)
            wait = WebDriverWait(self.browser, 20)
            project_link = wait.until(EC.visibility_of_element_located\
                                        ((By.XPATH, '//*[@id="tasks-table"]/tbody/tr/td[7]/a')))
            stage_status = self.browser.find_element_by_xpath(
                '//*[@id="tasks-table"]/tbody/tr/td[6]')
            self.assertEqual(stage_status.text, 'Assigned to consultant')
            project_link.click()
            accept_button = self.browser.find_element_by_xpath(
                '//*[@id="actionaccept"]')
            accept_button.click()
            accepted_by_consultant = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertEqual(accepted_by_consultant.text, 'Accepted by consultant')
            wait = WebDriverWait(self.browser, 10)
            confirm_visit_date = wait.until(EC.visibility_of_element_located\
                                        ((By.XPATH, '//*[@id="actionconfirmVisitDate"]')))
            confirm_visit_date.click()
            visit_date_confirmed = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertEqual(visit_date_confirmed.text, 'Visit date confirmed')
            comment_field = self.browser.find_element_by_xpath(
                 '//*[@id="record.comment"]')
            comment_field.send_keys('comment from Python')
            return_to_operator = self.browser.find_element_by_xpath(
                '//*[@id="actionreturnToOperator"]')
            return_to_operator.click()
            wait = WebDriverWait(self.browser, 10)
            jss_status = wait.until(EC.visibility_of_element_located\
                                        ((By.XPATH, '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')))
            self.assertEqual(jss_status.text, 'JSS')
        def test_e_5(self):
            self.login_as_operator()
            ref_num_search = self.browser.find_element_by_xpath(
                 '//*[@id="refNum"]')
            ref_num_search.send_keys(self.random_digits())
            search_button = self.browser.find_element_by_xpath(
                 '//*[@id="downloadProjects-form"]/div/div[1]/div[2]/div[3]/div/button')
            search_button.click()
            wait = WebDriverWait(self.browser, 20)
            jss_status = wait.until(EC.visibility_of_element_located\
                                         ((By.XPATH, '//*[@id="tasks-table"]/tbody/tr[1]/td[6]')))
            self.assertEqual(jss_status.text, 'JSS' )
            project_link = self.browser.find_element_by_xpath(
                '//*[@id="tasks-table"]/tbody/tr/td[7]/a')
            project_link.click()
            wait = WebDriverWait(self.browser, 20)
            assign_consultant = wait.until(EC.visibility_of_element_located\
                                         ((By.XPATH, '//*[@id="assignee-actions"]/div')))
            assign_consultant.click()
            assign_2_element = self.browser.find_element_by_xpath(
                '//*[@id="actionsAssignee"]')
            assign_2_element.click()
            consultant_1 = Select(self.browser.find_element_by_xpath(
                '//*[@id="actionsAssignee"]'))
            consultant_1.select_by_visible_text('consultant1')
            allocate = self.browser.find_element_by_id(
                'actionStage_ASSIGNED_TO_CONSULTANT')
            allocate.click()
            project_stage = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertEqual(project_stage.text, 'Assigned to consultant')
            # ASSERT FOR COMMENTS
            comment_field = self.browser.find_element_by_xpath(
                 '//*[@id="record.comment"]')
            # self.assertEqual(comment_field.text, 'comment from Python')

        def test_f_6(self):
            self.login_as_consultant_1()
            ref_num_search = self.browser.find_element_by_xpath(
                '//*[@id="refNum"]')
            ref_num_search.send_keys(self.random_digits())
            only_my_projects = self.browser.find_element_by_xpath(
                '//*[@id="myTasks1"]')
            only_my_projects.click()
            search_button = self.browser.find_element_by_xpath(
                '//*[@id="downloadProjects-form"]/div/div[1]/div[2]/div[3]/div/button')
            search_button.click()
            stage_status = self.browser.find_element_by_xpath(
                '//*[@id="tasks-table"]/tbody/tr[1]/td[6]')
            self.assertEqual(stage_status.text, 'Assigned to consultant')
            project_link = self.browser.find_element_by_xpath(
                '//*[@id="tasks-table"]/tbody/tr/td[7]/a')
            project_link.click()
            project_stage = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertEqual(project_stage.text, 'Assigned to consultant')
            accept_button = self.browser.find_element_by_xpath(
                '//*[@id="actionaccept"]')
            accept_button.click()
            accepted_by_consultant = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertEqual(accepted_by_consultant.text, 'Accepted by consultant')
            confirm_visit_date = self.browser.find_element_by_xpath(
                '//*[@id="actionconfirmVisitDate"]')
            confirm_visit_date.click()
            visit_date_confirmed = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertEqual(visit_date_confirmed.text, 'Visit date confirmed')
            start_work_on_site = self.browser.find_element_by_xpath(
                '//*[@id="actionworkOnSite"]')
            start_work_on_site.click()
            in_progress_status = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertEqual(in_progress_status.text, 'In progress')
            # Add file
            self.add_file()
            ready_for_qa = self.browser.find_element_by_xpath(
                '//*[@id="actionStage_READY_FOR_QA"]')
            ready_for_qa.click()
            # check Alert
            self.check_alert()
            return_to_in_progress = self.browser.find_element_by_xpath(
                '//*[@id="actionreturnToInProgress"]')
            return_to_in_progress.click()
            # check Value_is_required
            self.value_is_required()
            comment_field = self.browser.find_element_by_xpath(
                '//*[@id="record.comment"]')
            comment_field.send_keys('comment from Python')
            return_to_in_progress.click()
            in_progress_project = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertEqual(in_progress_project.text, 'In progress')
            # ASSERT FOR COMMENTS
            comment_field = self.browser.find_element_by_xpath(
                 '//*[@id="record.comment"]')
            # self.assertEqual(comment_field.text, 'comment from Python')
            ready_for_qa = self.browser.find_element_by_xpath(
                '//*[@id="actionStage_READY_FOR_QA"]')
            ready_for_qa.click()
            qa_1 = Select(self.browser.find_element_by_xpath(
                '//*[@id="actionsAssignee"]'))
            qa_1.select_by_visible_text('qa1')
            qa_assigned = self.browser.find_element_by_xpath(
                '//*[@id="actionqaAssigned"]')
            qa_assigned.click()
            time.sleep(5)
            qa = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertEqual(qa.text, 'QA')
            participant_field = self.browser.find_element_by_xpath(
                '//*[@id="participant-table"]/tbody/tr/td[2]')
            self.assertEqual(participant_field.text, 'qa1')
        def test_g_7(self):
            self.login_as_operator()
            ref_num_search = self.browser.find_element_by_xpath(
                '//*[@id="refNum"]')
            ref_num_search.send_keys(self.random_digits())
            check_box = self.browser.find_element_by_xpath('//*[@id="myTasks1"]')
            check_box.click()
            search_button = self.browser.find_element_by_xpath(
                '//*[@id="downloadProjects-form"]/div/div[1]/div[2]/div[3]/div/button')
            search_button.click()
            time.sleep(10)
            qa_stage = self.browser.find_element_by_xpath(
                '//*[@id="tasks-table"]/tbody/tr/td[6]')
            self.assertEqual(qa_stage.text, 'QA')
            project_link = self.browser.find_element_by_xpath(
                '//*[@id="tasks-table"]/tbody/tr/td[7]/a')
            project_link.click()
            qa_project_stage = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertEqual(qa_project_stage.text, 'QA')
            rollback_button = self.browser.find_element_by_xpath(
                '//*[@id="actionrollback"]')
            rollback_button.click()
            # check Value_is_required
            self.value_is_required()
            self.send_comments()
            rollback_button.click()
            time.sleep(5)
            rollback_stage_field = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertEqual(rollback_stage_field.text, 'Rollback')

        def test_h_8(self):
            self.login_as_operator()
            ref_num_search = self.browser.find_element_by_xpath(
                '//*[@id="refNum"]')
            ref_num_search.send_keys(self.random_digits())
            search_button = self.browser.find_element_by_xpath(
                '//*[@id="downloadProjects-form"]/div/div[1]/div[2]/div[3]/div/button')
            search_button.click()
            time.sleep(5)
            project_link = self.browser.find_element_by_xpath(
                '//*[@id="tasks-table"]/tbody/tr/td[7]/a')
            project_link.click()
            time.sleep(10)
            rollback_stage_field = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertEqual(rollback_stage_field.text, 'Rollback')
            return_to_QA = self.browser.find_element_by_xpath(
                '//*[@id="actionStage_QA"]')
            return_to_QA.click()
            # check Value_is_required
            self.value_is_required()
            self.send_comments()
            return_to_QA.click()
            qa = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertEqual(qa.text, 'QA')
        def test_i_9(self):
            self.login_as_operator()
            ref_num_search = self.browser.find_element_by_xpath(
                '//*[@id="refNum"]')
            ref_num_search.send_keys(self.random_digits())
            search_button = self.browser.find_element_by_xpath(
                '//*[@id="downloadProjects-form"]/div/div[1]/div[2]/div[3]/div/button')
            search_button.click()
            time.sleep(5)
            project_link = self.browser.find_element_by_xpath(
                '//*[@id="tasks-table"]/tbody/tr/td[7]/a')
            project_link.click()
            time.sleep(5)
            qa = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]')
            self.assertEqual(qa.text, 'QA')
            qa_complete = self.browser.find_element_by_xpath('//*[@id="actioncomplete"]')
            qa_complete.click()
            qa_complete_stage = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertEqual(qa_complete_stage.text, 'QA complete')
        def test_j_10(self):
            self.login_as_operator()
            ref_num_search = self.browser.find_element_by_xpath(
                '//*[@id="refNum"]')
            ref_num_search.send_keys(self.random_digits())
            search_button = self.browser.find_element_by_xpath(
                '//*[@id="downloadProjects-form"]/div/div[1]/div[2]/div[3]/div/button')
            search_button.click()
            time.sleep(5)
            project_link = self.browser.find_element_by_xpath(
                '//*[@id="tasks-table"]/tbody/tr/td[7]/a')
            project_link.click()
            time.sleep(5)
            qa_complete_stage = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertEqual(qa_complete_stage.text, 'QA complete')
            sign_off = self.browser.find_element_by_xpath(
                '//*[@id="actionStage_SIGNED_OFF_AS_FINAL"]')
            sign_off.click()
            signed_off_as_final = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertEqual(signed_off_as_final.text, 'Signed off as final')
            reopen_project = self.browser.find_element_by_xpath(
                '//*[@id="actionreopen"]')
            reopen_project.click()
            qa_complete_stage = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertEqual(qa_complete_stage.text, 'QA complete')
            sign_off = self.browser.find_element_by_xpath(
                '//*[@id="actionStage_SIGNED_OFF_AS_FINAL"]')
            sign_off.click()
            signed_off_as_final = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertEqual(signed_off_as_final.text, 'Signed off as final')
            send_to_client = self.browser.find_element_by_xpath(
                '//*[@id="actionsendToClient"]')
            send_to_client.click()
            sent_to_client_stage = self.browser.find_element_by_xpath(
                '//*[@id="projectTable"]/tbody/tr[2]/td[2]/div/div[2]/span')
            self.assertEqual(sent_to_client_stage.text, 'Sent to client')
            self.browser.execute_script("window.scrollTo(0, 1000)")
            domument_is_present = self.browser.find_element_by_xpath(
                '//*[@id="doc-table"]/tbody/tr/td[1]/a')
            self.assertEqual(domument_is_present.text, 'images.jpg')
            comments_are_present = self.browser.find_element_by_xpath(
                '//*[@id="comments-table"]/tbody/tr[5]/td[1]')
            self.assertEqual(comments_are_present.text, 'comment from Python')
            edit_project_story = self.browser.find_element_by_xpath(
                '//*[@id="audit-table"]/tbody/tr[5]/td[1]')
            self.assertEqual(edit_project_story.text, 'EDIT')
            elem = self.browser.find_element_by_tag_name('a')
            elem.send_keys(Keys.PAGE_DOWN)
            export_button = self.browser.find_element_by_xpath(
                '//*[@id="actionexportToPrism"]')
            self.assertEqual(export_button.text, 'Export to Prism')



        def tearDown(self):
            self.browser.close()
if __name__ == '__main__':
    nose.run(defaultTest="", argv=TEST_PARAMS)


