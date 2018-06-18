from selenium import webdriver
# create a new Firefox session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
# navigate to the application home page
driver.get("https://tetra-qa.strikersoft.com/operational")
# get the search textbox
search_field = driver.find_element_by_id("login")
search_field.send_keys("tetra-support@strikersoft.com")
pass_field = driver.find_element_by_id("password")
pass_field.send_keys("Qqq!1234")
# enter search keyword and submit
# search_field.send_keys("phones")
# search_field.submit()
submit_button = driver.find_element_by_xpath("//*[@id='loginForm']/button")
submit_button.click()
driver.implicitly_wait(30)
# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method
products = driver.find_elements_by_xpath("//select[@id='typesHSF']")
# get the number of anchor elements found
print "Found " + str(len(products)) + " products:"
# iterate through each anchor element and print the text that is
# name of the product
for product in products:
    print product.text
# close the browser window
driver.quit()