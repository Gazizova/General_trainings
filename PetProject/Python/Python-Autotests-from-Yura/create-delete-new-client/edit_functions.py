from random import randint
import nose

__author__ = 'yuriy@strikersoft.com'
__description__ = "Tetra test"

edit_random_value = randint(10 ** (5 - 1), (10 ** 5) - 1)
edit_random_for_region = randint(10 ** (4 - 1), (10 ** 4) - 1)
edit_random_value_lanlords = randint(10 ** (5 - 1), (10 ** 5) - 1)
edit_random_new_lanlords = randint(10 ** (5 - 1), (10 ** 5) - 1)
edit_random_area_of_compliance = randint(10 ** (4 - 1), (10 ** 4) - 1)
edit_random_task_group = randint(10 ** (5 - 1), (10 ** 5) - 1)
edit_random_code_task_status = randint(10 ** (5 - 1), (10 ** 5) - 1)
edit_random_code_task_repository = randint(10 ** (5 - 1), (10 ** 5) - 1)
edit_random_taskinterval_digits = randint(10 ** (2 - 1), (10 ** 2) - 1)
edit_random_not_due_digits = randint(10 ** (2 - 1), (10 ** 2) - 1)
edit_random_task_digits = randint(10 ** (5 - 1), (10 ** 5) - 1)
edit_random_add_action = randint(10 ** (5 - 1), (10 ** 5) - 1)
edit_random_supplier_business = randint(10 ** (5 - 1), (10 ** 5) - 1)
edit_random_accident_category = randint(10 ** (5 - 1), (10 ** 5) - 1)
edit_random_email_notification = randint(10 ** (5 - 1), (10 ** 5) - 1)
edit_random_supplier = randint(10 ** (5 - 1), (10 ** 5) - 1)
edit_random_client_users = randint(10 ** (5 - 1), (10 ** 5) - 1)
edit_roles = randint(10 ** (5 - 1), (10 ** 5) - 1)
edit_action_status = randint(10 ** (5 - 1), (10 ** 5) - 1)
edit_property_portfolio = randint(10 ** (5 - 1), (10 ** 5) - 1)

class EditFunctions(object):

    def __init__(self):
        pass

    def edit_roles_digits(self):
        return edit_roles

    # metod for assert
    def get_edit_roles_digits(self):
        return edit_roles

    def edit_property_portfolio(self):
        return edit_property_portfolio

    # metod for assert
    def get_edit_property_portfolio(self):
        return edit_property_portfolio

    def random_edit_action_status(self):
        return edit_action_status

    # metod for assert
    def get_random_edit_action_status(self):
        return edit_action_status

    def edit_random_digits(self):
        return edit_random_value

    # metod for assert
    def get_edit_random_digits(self):
        return edit_random_value

    def edit_random_supplier_digits(self):
        return edit_random_supplier_business

    # metod for assert
    def get_edit_random_supplier_digits(self):
        return edit_random_supplier_business

    def edit_random_client_users(self):
        return edit_random_client_users

    # metod for assert
    def get_edit_random_client_users(self):
        return edit_random_client_users

    def edit_random_supplier_business(self):
        return edit_random_supplier

    # metod for assert
    def get_random_supplier(self):
        return edit_random_supplier

    def edit_random_add_accident_category(self):
        return edit_random_accident_category

    # metod for assert
    def get_edit_random_add_accident_category(self):
        return edit_random_accident_category

    def edit_random_digits_add_action(self):
        return edit_random_add_action

    # metod for assert
    def get_edit_random_digits_add_action(self):
        return edit_random_add_action

    def edit_random_not_due_yet_multiplier(self):
        return edit_random_not_due_digits

    # metod for assert
    def get_edit_random_not_due_yet_multiplier(self):
        return edit_random_not_due_digits

    def edit_task_interval_multiplier(self):
        return edit_random_taskinterval_digits

    # metod for assert
    def get_edit_task_interval_multiplier(self):
        return edit_random_taskinterval_digits

    def edit_random_digits_regions(self):
        return edit_random_for_region

    # metod for assert
    def get_edit_random_digits_regions(self):
        return edit_random_for_region

    def edit_random_digits_for_lanlords(self):
        return edit_random_value_lanlords

    # metod for assert
    def get_edit_random_digits_for_lanlords(self):
        return edit_random_value_lanlords

    def edit_random_digits_new_lanlord(self):
        return edit_random_new_lanlords

    # metod for assert
    def get_edit_random_digits_new_lanlord(self):
        return edit_random_new_lanlords

    def edit_random_digits_area_of_compliance(self):
        return edit_random_area_of_compliance

    # metod for assert
    def get_edit_random_digits_area_of_compliance(self):
        return edit_random_area_of_compliance

    def edit_random_digits_task_group(self):
        return edit_random_task_group

    # metod for assert
    def get_edit_random_digits_task_group(self):
        return edit_random_task_group

    def edit_random_digits_task_status(self):
        return edit_random_code_task_status

    # metod for assert
    def get_edit_random_digits_task_status(self):
        return edit_random_code_task_status

    def edit_random_digits_new_repository(self):
        return edit_random_code_task_repository

    # metod for assert
    def get_edit_random_digits_new_repository(self):
        return edit_random_code_task_repository

    def edit_random_digits_task(self):
        return edit_random_task_digits

    # metod for assert
    def get_edit_random_digits_task(self):
        return edit_random_task_digits

    def edit_email_notification_config(self):
        return edit_random_email_notification

    # metod for assert
    def get_edit_email_notification_config(self):
        return edit_random_email_notification

