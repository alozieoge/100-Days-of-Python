from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import time, sleep

chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url="http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id(id_="cookie")

start_time = time()
current_time = time()
buy_time = 10
game_time = 5 * 60
n = 1

while current_time <= start_time + game_time:
    while current_time <= start_time + (n * buy_time):
        cookie.click()
        current_time = time()

    money_element = driver.find_element_by_id(id_="money")
    money = int(money_element.text.replace(',', ''))
    print(f"Money: {money}")

    store_items = driver.find_elements_by_css_selector(css_selector="#store b")
    store_items = store_items[:-1][::-1]

    for item in store_items:
        if item.get_attribute("class") != "grayed":
            item_name = item.text.split("-")[0].strip()
            item_cost = int(item.text.split("-")[-1].strip().replace(",", ""))
            if money > item_cost:
                print(f"Item: {item_name}, Cost: {item_cost}")
                item.click()
                break

    current_time = time()
    n += 1

current_time = time()
cookies_per_second = driver.find_element_by_css_selector(css_selector="#saveMenu #cps")
print(f"\n{cookies_per_second.text}")
print(f"Completed in {int((current_time - start_time) / 60)} minutes, {round((current_time - start_time) % 60, 2)} seconds")

# driver.quit()

# cookies/second : 86.2
