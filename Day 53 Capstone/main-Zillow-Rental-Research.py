
import requests
from bs4 import BeautifulSoup
import lxml
from pprint import pprint
from data_entry import DataEntry

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"

request_header = {
    "accept": "",
    "accept-encoding": "",
    "accept-language": "",
    "upgrade-insecure-requests": "",
    "user-agent": "",
}

response = requests.get(url=ZILLOW_URL, headers=request_header)
response.raise_for_status()
# print(response.status_code)
zillow_web_page = response.text

soup = BeautifulSoup(markup=zillow_web_page, parser="html.parser", features="lxml")
# print(soup.prettify())
rental_listings = soup.find_all("div", class_="list-card-info")

# print(len(rental_listings))
house_links = []
house_addresses = []
house_prices = []

for listing in rental_listings:
    link = listing.find(name="a", class_="list-card-link").get(key="href")
    if link.startswith("/b"):
        link = "https://www.zillow.com" + link
    house_links.append(link)
    address = listing.select_one(selector=".list-card-addr").getText()
    house_addresses.append(address)
    price = listing.select_one(selector="div div .list-card-price").getText().replace("+", "/").split('/')[0]
    house_prices.append(price)

print(house_links)
print(house_addresses)
print(house_prices)

data_entry = DataEntry()
for i, (address, price, link) in enumerate(zip(house_addresses, house_prices, house_links)):
    data_entry.answer_form(address, price, link)
    print(f"Response {i + 1} entered.")

# data_entry.data_to_sheet()





