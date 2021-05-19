import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import time, sleep

chrome_driver_path = "C:/Development/chromedriver.exe"

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url="https://www.linkedin.com/jobs/search/...")


sign_in = driver.find_element_by_class_name(name="nav__button-secondary")
sign_in.click()
sleep(3)

username_field = driver.find_element_by_id(id_="username")
password_field = driver.find_element_by_id(id_="password")
sign_in_button = driver.find_element_by_class_name(name="btn__primary--large")

username_field.send_keys(username)
password_field.send_keys(password)
sign_in_button.send_keys(Keys.ENTER)
sleep(3)

job = driver.find_element_by_link_text(link_text="Full Stack Python Developer")
job.click()
sleep(2)

apply_button = driver.find_element_by_css_selector(css_selector=".jobs-details-top-card__actions-container .jobs-apply-button")
apply_button.click()
sleep(3)

try:
    submit = driver.find_element_by_css_selector(css_selector=".jobs-easy-apply-modal .jobs-easy-apply-content .artdeco-button")
except NoSuchElementException as e:
    print(e.msg)
else:
    submit.click()

    try:
        follow_company = driver.find_element_by_css_selector(css_selector="footer .ph5 label")
    except NoSuchElementException as e:
        print(e.msg)
    else:
        follow_company.click()
        sleep(1)

        try:
            submit = driver.find_element_by_css_selector(css_selector="footer .artdeco-button--primary")
        except NoSuchElementException as e:
            print(e.msg)
        else:
            submit.click()

# driver.quit()
