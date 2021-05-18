from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element_by_css_selector(css_selector="#articlecount a")

# print(article_count.text)
# article_count.click()

# To search for a link by its text
all_portals = driver.find_element_by_link_text(link_text="All portals")
# all_portals.click()

# To type in an input field and submit
search = driver.find_element_by_name(name="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)


# driver.quit()
