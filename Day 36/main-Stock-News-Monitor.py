import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_api_key = ""
news_api_key = ""

account_sid = ""
auth_token = ""

from_number = ""
to_number = ""

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "datatype": "json",
    "apikey": stock_api_key,
}

news_params = {
    "apiKey": news_api_key,
    "q": COMPANY_NAME,
    "from": "2021-05-05",
    "to": "2021-05-05",
    "language": "en"
}

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
print(stock_response.status_code)
stock_response.raise_for_status()
stock_data = stock_response.json()
print(stock_data)

# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two
# prices. e.g. 40 - 20 = -20, but the positive difference is 20.
first_day = "2021-05-05"
next_day = "2021-05-05"

# print(stock_data["Time Series (Daily)"][day0]["4. close"])
first_day_closing = float(stock_data["Time Series (Daily)"][first_day]["4. close"])
next_day_closing = float(stock_data["Time Series (Daily)"][next_day]["4. close"])

pos_difference = abs(first_day_closing - next_day_closing)

# HINT 2: Work out the value of 5% of yesterday's closing stock price.
five_percent_closing = 0.05 * first_day_closing
print(five_percent_closing)
percent_change = round(pos_difference * 100 / first_day_closing, 1)

diff_sign = ""
if first_day_closing >= next_day_closing:
    diff_sign = "🔻"
else:
    diff_sign = "🔺"


# STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
print(news_response.status_code)
news_response.raise_for_status()
news_data = news_response.json()
# print(news_data)

# HINT 1: Think about using the Python Slice Operator
first_3_articles = news_data["articles"][:3]
print(first_3_articles)


# STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
# HINT 1: Consider using a List Comprehension.
client = Client(account_sid, auth_token)

for article in first_3_articles:
    print(f"TSLA: {diff_sign} {percent_change}% \nHeadline: {article['title']}. \nBrief: {article['description']}")
    message = client.messages.create(
        body=f"\nTSLA: {diff_sign} {percent_change}% \nHeadline: {article['title']}. \nBrief: {article['description']}",
        from_=from_number,
        to=to_number)

    print(message.sid)


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

