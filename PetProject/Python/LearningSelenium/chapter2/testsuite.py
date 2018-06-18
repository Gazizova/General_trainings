import unittest
import HTMLTestRunner
import os
from LearningSelenium.chapter2.startpage import TestSearchTests

# get the directory path to output report file
dir = os.getcwd()
# from homepagetests import HomePageTest
# get all tests from class
search_tests = unittest.TestLoader().loadTestsFromTestCase(TestSearchTests)

# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([search_tests])

# open the report file
outfile = open(dir + "\SmokeTestReport.html", "w")
# unittest.TextTestRunner(verbosity=2).run(smoke_tests)
# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(
    stream=outfile,
    title='Test Report',
    description="Smoke Tests",
    )
runner.run(smoke_tests)