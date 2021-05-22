import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

CHROME_DRIVER_PATH = "C:/Development/chromedriver.exe"

INSTAGRAM_URL = "https//www.instagram.com"

# INSTAGRAM_EMAIL = os.environ.get("INSTAGRAM_EMAIL")
# INSTAGRAM_PASSWORD = os.environ.get("INSTAGRAM_PASSWORD")

TARGET_ACCOUNT = ""


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.implicitly_wait(time_to_wait=10)
        self.driver.maximize_window()

        self.driver.get(url=INSTAGRAM_URL)
        self.followers = 0
        self.followers_window = None

    def login(self):
        insta_username = self.driver.find_element_by_xpath(xpath='//label/input[@name="username"]')
        insta_password = self.driver.find_element_by_xpath(xpath='//label/input[@name="password"]')
        insta_login_button = self.driver.find_element_by_xpath(xpath='//button/div[text()="Log In"]')
        insta_login_button.click()
        sleep(2)

        no_save_login = self.driver.find_element_by_xpath(xpath='//button[text()="Not Now"]')
        no_save_login.click()
        sleep(2)

        no_notification = self.driver.find_element_by_xpath(xpath='//button[text()="Not Now"]')
        no_notification.click()
        sleep(2)

    def find_followers(self):
        self.driver.get(url=INSTAGRAM_URL + "/" + TARGET_ACCOUNT)

        followers_button = self.driver.find_element_by_xpath(xpath='//a[@href="/chefsteps/followers/"]')
        self.followers = int(followers_button.get_attribute(name="title").replace(",", ""))

        followers_button.click()
        self.scroll_down(scrolls=5)

    def scroll_down(self, scrolls):
        # Scroll down through followers list
        self.followers_window = self.driver.find_element_by_xpath(xpath='/html/body/div[5]/div/div/div[2]')
        for i in range(scrolls):
            self.followers_window.send_keys(Keys.END)
            sleep(2)

    def follow(self, start_count=0):
        follower_buttons = self.driver.find_elements_by_xpath(xpath='//div/button[text()="Follow"]')

        for follower in follower_buttons[start_count:]:
            try:
                follower.click()
                sleep(2)
            except ElementClickInterceptedException:
                sleep(1)
                cancel_followed = self.driver.find_element_by_xpath(xpath='//div/button[text()="Cancel"]')
                cancel_followed.click()
                sleep(1)

            start_count += 1

        # if start_count < self.followers:
        #     self.scroll_down(scrolls=1)
        #     sleep(2)
        #     self.follow(start_count=start_count)




