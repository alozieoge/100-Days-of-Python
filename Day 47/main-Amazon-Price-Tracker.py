import os
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

product_url = "https://www.amazon.co.uk/New-Apple-iPhone-Pro-128GB/dp/B08L5SVK83/ref=sr_1_3?crid=26F2TOQ5BPUHC&d" \
              "child=1&keywords=iphone%2B12%2Bpro%2Bmax&qid=1621276039&sprefix=iphon%2Caps%2C173&sr=8-3&th=1"

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "",
}

sender_email = os.environ.get("SENDER_EMAIL")
sender_password = os.environ.get("SENDER_PASSWORD")
receiver_email = os.environ.get("RECEIVER_EMAIL")

smtp_host = os.environ.get("SMTP_HOST")

price_threshold = 1200.0


# Scrape Amazon product webpage
response = requests.get(url=product_url, headers=headers)
product_webpage = response.text

# Make a soup from the HTML text
soup = BeautifulSoup(markup=product_webpage, parser="html.parser", features="lxml")
# print(soup.prettify())

# Get product price
price_tag = soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString")
price = float("".join(price_tag.getText()[1:].split(",")))

# Get the product title
title_tag = soup.find(name="span", class_="a-size-large product-title-word-break")
title = title_tag.getText().strip()

# Send an email if the price is right.
if price < price_threshold:
    message = f"Subject:Amazon Price Alert\n\n'{title}' is now £{price}\n{product_url}"

    with smtplib.SMTP_SSL(host=smtp_host, port=465) as connection:
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(from_addr=sender_email,
                            to_addrs=receiver_email,
                            msg=message.encode("utf-8"))


