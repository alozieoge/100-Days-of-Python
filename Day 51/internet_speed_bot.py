import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

CHROME_DRIVER_PATH = "C:/Development/chromedriver.exe"
SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/"

TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")


class InternetSpeedBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.implicitly_wait(time_to_wait=10)
        self.driver.maximize_window()

        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(url=SPEED_TEST_URL)

        cookies_consent = self.driver.find_element_by_xpath(xpath='//button[@id="_evidon-banner-acceptbutton"]')
        cookies_consent.click()
        speed_test_go = self.driver.find_element_by_css_selector(
            css_selector=".js-start-test.test-mode-multi span.start-text")
        speed_test_go.click()

        sleep(50)

        download_speed = self.driver.find_element_by_css_selector(css_selector=".result-data-large.download-speed")
        self.down = float(download_speed.text)
        upload_speed = self.driver.find_element_by_css_selector(css_selector=".result-data-large.upload-speed")
        self.up = float(upload_speed.text)

    def tweet_at_provider(self, tweet):
        self.driver.get(url=TWITTER_URL)

        twitter_login = self.driver.find_element_by_xpath(xpath='//span[text()="Log in"]')
        twitter_login.click()

        twitter_username = self.driver.find_element_by_xpath(xpath='//input[@name="session[username_or_email]"]')
        twitter_password = self.driver.find_element_by_xpath(xpath='//input[@name="session[password]"]')

        twitter_username.send_keys(TWITTER_EMAIL)
        twitter_password.send_keys(TWITTER_PASSWORD)
        twitter_password.send_keys(Keys.ENTER)

        sleep(2)

        tweet_box = self.driver.find_element_by_css_selector(css_selector="div.public-DraftStyleDefault-block")
        sleep(2)
        tweet_button = self.driver.find_element_by_xpath(xpath='//div[@data-testid="tweetButtonInline"]')

        tweet_box.send_keys(tweet)
        tweet_button.click()


