import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_driver_path = "C:/Development/chromedriver.exe"

fb_email = os.environ.get("FB_EMAIL")
fb_password = os.environ.get("FB_PASSWORD")

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get(url="https://tinder.com/")
sleep(2)

login = driver.find_element_by_xpath(xpath='//*[@id="c-174738105"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()
sleep(2)

login_with_fb = driver.find_element_by_xpath(xpath='//*[@id="c-1903119181"]/div/div/div[1]/div/div[3]/span/div[2]/button')
login_with_fb.click()
sleep(2)

# Accept Facebook cookies
open_windows = driver.window_handles
tinder_window = open_windows[0]
fb_cookies_window = open_windows[-1]
driver.switch_to.window(fb_cookies_window)
print(len(open_windows))
print(driver.title)
accept_cookies_button = driver.find_element_by_xpath(xpath='//*[@title="Accept All"]')
accept_cookies_button.click()
sleep(2)

# Log into Facebook
fb_email_input = driver.find_element_by_xpath(xpath='//input[@id="email"]')
fb_email_input.send_keys(fb_email)

fb_password_input = driver.find_element_by_xpath(xpath='//input[@id="pass"]')
fb_password_input.send_keys(fb_password)

fb_login_button = driver.find_element_by_xpath(xpath='//*[@name="login"]')
fb_login_button.click()

confirm_button = driver.find_element_by_xpath(xpath='//button[@name="__CONFIRM__"]')
confirm_button.click()

sleep(3)

# Switch back to Tinder
driver.switch_to.window(tinder_window)
print(driver.title)

# To be continued because of Facebook time restrictions for new accounts


# driver.quit()
