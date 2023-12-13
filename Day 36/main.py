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
    difference = abs(float(f_value) - float(s_value))
    return (difference / float(max(f_value, s_value))) * 100 >= 5


if is_five_percent_difference(yesterday_close_price, before_yesterday_close_price):
    # connect to the news api and get three articles
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything?"
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
    print(articles)
