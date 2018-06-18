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

__author__ = 'Alyona'
__description__ = "Tetra test"

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

