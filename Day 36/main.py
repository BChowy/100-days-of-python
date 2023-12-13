import os
import requests
from datetime import datetime
from datetime import timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

today = datetime.today().date()
yesterday_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
before_yesterday_date = (today - timedelta(days=2)).strftime('%Y-%m-%d')

ALPHA_ADVANTAGE_KEY = os.environ.get("ALPHA_ADVANTAGE_KEY")
NEWS_API_KEY = "712d241f07924bf0866e7174313710a8"

ALPHA_ADVANTAGE_API = "https://www.alphavantage.co/query?"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_ADVANTAGE_KEY,
}

def is_five_percent_difference(f_value, s_value):
    difference = max(f_value, s_value) - min(f_value, s_value)
    median = (f_value + s_value) / 2
    return (difference / median) * 100 >= 5

response = requests.get(ALPHA_ADVANTAGE_API, params=parameters)
response.raise_for_status()
yesterday_close = response.json()["Time Series (Daily)"][yesterday_date]["4. close"]
before_yesterday_close = response.json()["Time Series (Daily)"][before_yesterday_date]["4. close"]

print(yesterday_close)
print(before_yesterday_close)


## STEP 1: Use https://newsapi.org
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://www.alphavantage.co
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
