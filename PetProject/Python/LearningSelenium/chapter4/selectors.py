from selenium import webdriver

class Selectors():
    # def sel(self):
    #     driver = webdriver.Chrome()

        global project_code
        project_code = webdriver.find_element_by_id("record.code")

        global note
        note = webdriver.find_element_by_id("record.note")
        global address
        address = webdriver.find_element_by_id("record.property.address2")
        global client
        client = webdriver.find_element_by_id("record.property.clientName")
        global contact
        contact = webdriver.find_element_by_id("record.propertyContactDto.name")
