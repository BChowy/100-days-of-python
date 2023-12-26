from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.select(selector="span.titleline > a")
# articles_score = soup.select(selector="span.score")

titles = []
links = []

for article in articles:
    titles.append(article.get_text())
    links.append(article.get("href"))

scores = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]

max_score = max(scores)
max_score_index = scores.index(max_score)

print(titles[max_score_index])
print(links[max_score_index])
