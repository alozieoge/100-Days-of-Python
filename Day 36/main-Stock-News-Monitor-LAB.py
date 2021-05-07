import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""

ACCOUNT_SID = ""
AUTH_TOKEN = ""

FROM_NUMBER = ""
TO_NUMBER = ""

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
# print(stock_response.json())
data = stock_response.json()["Time Series (Daily)"]
# print(data)
data_list = [value for (key, value) in data.items()]
# print(data_list)
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
print(yesterday_closing_price)

# TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
print(day_before_yesterday_closing_price)

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
print(positive_difference)

difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((positive_difference / yesterday_closing_price) * 100, 1)
print(diff_percent)

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diff_percent > 1:
    print("Get News")

# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if diff_percent > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    # print(news_response.json())
    articles = news_response.json()["articles"]
    # print(articles)

    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.
    # Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    # print(three_articles)

    # STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.
    # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    # f"TSLA: {diff_sign} {percent_change}% \nHeadline: {article['title']}. \nBrief: {article['description']}"
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent} \nHeadline: {article['title']}. " \
                          f"\nBrief: {article['description']}" for article in three_articles]

    # TODO 9. - Send each article as a separate message via Twilio.
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for article in formatted_articles:
        # print(article)
        message = client.messages.create(
            body=article,
            from_=FROM_NUMBER,
            to=TO_NUMBER)

        print(message.sid)

# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

