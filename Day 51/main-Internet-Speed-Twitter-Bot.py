from internet_speed_bot import InternetSpeedBot

PROMISED_DOWN = 250
PROMISED_UP = 300

internet_speed_bot = InternetSpeedBot()

internet_speed_bot.get_internet_speed()
print(f"down: {internet_speed_bot.down}")
print(f"up: {internet_speed_bot.up}")

if internet_speed_bot.up < PROMISED_UP and internet_speed_bot.down < PROMISED_DOWN:
    tweet = f"Hey ISP, why is my internet speed {internet_speed_bot.down} down / {internet_speed_bot.up} up, when " \
            f"I pay for {PROMISED_DOWN} down / {PROMISED_UP} up?"

    internet_speed_bot.tweet_at_provider(tweet=tweet)


