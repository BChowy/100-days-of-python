from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "SPOTIFY CLIENT ID"
CLIENT_SECRET = "SPOTIFY CLIENT SECRET"

url = "https://www.billboard.com/charts/hot-100/"

date = input("Enter a date in the format of YYYY-MM-DD:: ")

date_url = f"{url}{date}"

response = requests.get(date_url)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select(selector="div.o-chart-results-list-row-container > ul > li h3#title-of-a-story")

songs_list = [title.get_text().strip() for title in titles]

# print(songs_list)
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user_id, f"date Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
