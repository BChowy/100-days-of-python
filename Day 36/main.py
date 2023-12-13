import os
import requests
from datetime import datetime
from datetime import timedelta
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query?"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything?"

TWILIO_NUMBER = "virtual twilio number"
VERIFIED_NUMBER = "phone number verified with Twilio"

# Both works
STOCK_API_KEY = os.environ.get("ALPHA_ADVANTAGE_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_SID = "TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "TWILIO AUTH TOKEN"

# Get dates
today = datetime.today().date()
yesterday_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
before_yesterday_date = (today - timedelta(days=2)).strftime('%Y-%m-%d')

# Connect to the stock endpoint
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

# Get yesterday and the day before it closing prices
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
yesterday_close_price = response.json()["Time Series (Daily)"][yesterday_date]["4. close"]
before_yesterday_close_price = response.json()["Time Series (Daily)"][before_yesterday_date]["4. close"]


# Find the positive difference between prices
difference = float(yesterday_close_price) - float(before_yesterday_close_price)
diff_percentage = (abs(difference) / float(max(yesterday_close_price, before_yesterday_close_price))) * 100

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if diff_percentage >= 5:
    # connect to the news api and get three articles
    news_params = {
        "qInTitle": COMPANY_NAME,
        "language": "en",
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY,
    }

    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    # Need only top three articles
    articles = response.json()["articles"][:3]

    formatted_articles = [
        f"{STOCK}: {up_down}{round(diff_percentage)}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for
        article in articles]
    print(formatted_articles)
    # Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
