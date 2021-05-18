from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url="http://secure-retreat-92358.herokuapp.com/")

first_name = ""
last_name = ""
email_address = ""

f_name = driver.find_element_by_name(name="fName")
l_name = driver.find_element_by_name(name="lName")
email = driver.find_element_by_name(name="email")
signup = driver.find_element_by_class_name(name="btn-block")

f_name.send_keys(first_name)
l_name.send_keys(last_name)
email.send_keys(email_address)
signup.click()
# signup.send_keys(Keys.ENTER)

# driver.quit()

