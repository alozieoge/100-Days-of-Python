import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import time, sleep
from pprint import pprint

chrome_driver_path = "C:/Development/chromedriver.exe"

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()

driver.get(url="https://www.linkedin.com/jobs/search/...")
sleep(2)

# Sign in
# Locate sign in button
sign_in = driver.find_element_by_class_name(name="nav__button-secondary")
sign_in.click()
sleep(2)

# Locate sign in input fields
username_field = driver.find_element_by_id(id_="username")
password_field = driver.find_element_by_id(id_="password")
sign_in_button = driver.find_element_by_class_name(name="btn__primary--large")

# Provide username and password and proceed
username_field.send_keys(username)
password_field.send_keys(password)
sign_in_button.send_keys(Keys.ENTER)
sleep(3)

# Get list of jobs returned from the search
try:
    # job_links = driver.find_elements_by_css_selector(
    #     css_selector=".jobs-search-results__list-item .artdeco-entity-lockup__content")
    job_listings = driver.find_elements_by_css_selector(
        css_selector=".job-card-container--clickable")
    print(f"{len(job_listings)} jobs found!\n")
except NoSuchElementException as e:
    print(e.msg)
    print("No job list found")
else:
    for job in job_listings:
        job_title = job.find_element_by_class_name(name="job-card-list__title")
        job_company = job.find_element_by_class_name(name="job-card-container__company-name")
        job_location = job.find_element_by_css_selector(
            css_selector=".artdeco-entity-lockup__caption .job-card-container__metadata-item")
        try:
            job_salary = job.find_element_by_css_selector(
                css_selector=".artdeco-entity-lockup__metadata .job-card-container__metadata-item")
        except NoSuchElementException as e:
            job_salary_text = "No salary"
        else:
            job_salary_text = job_salary.text
        finally:
            pprint({"title": job_title.text,
                    "company": job_company.text,
                    "location": job_location.text,
                    "salary": job_salary_text,
                    })
            print("")

# driver.quit()
