import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")
GOOGLE_FORM_URL = os.environ.get("GOOGLE_FORM_URL")
EDIT_FORM_URL = os.environ.get("EDIT_FORM_URL")


class DataEntry:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.implicitly_wait(time_to_wait=10)
        self.driver.maximize_window()

        self.driver.get(url=GOOGLE_FORM_URL)

    def answer_form(self, address, price, link):
        self.driver.get(url=GOOGLE_FORM_URL)

        address_input = self.driver.find_element_by_xpath(xpath='//input[@aria-describedby="i2 i3"]')
        price_input = self.driver.find_element_by_xpath(xpath='//input[@aria-describedby="i6 i7"]')
        link_input = self.driver.find_element_by_xpath(xpath='//input[@aria-describedby="i10 i11"]')
        submit_button = self.driver.find_element_by_css_selector(css_selector='span.exportButtonContent')
        sleep(1)

        address_input.send_keys(address)
        price_input.send_keys(price)
        link_input.send_keys(link)
        submit_button.click()
        sleep(1)

    def data_to_sheet(self):
        self.driver.get(url=EDIT_FORM_URL)

        response_tab = self.driver.find_element_by_css_selector(css_selector='div.freebirdFormeditorViewTabResponsesViewTabContent')
        response_tab.click()
        sleep(1)

        create_spreadsheet = self.driver.find_element_by_css_selector(css_selector='div.freebird-qp-icon-spreadsheet-green')
        create_spreadsheet.click()
        sleep(1)



