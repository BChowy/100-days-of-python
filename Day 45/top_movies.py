from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
titles.reverse()

with open ("movies.txt", "w") as file:
    for title in titles:
        file.write(f"{title.get_text()}\n")