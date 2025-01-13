import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

BREAK_KEY = "SFG8YG0AUHvn0d8qygk3fhao81111111111"

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id="7822b25bde0c45ab8d566b23d88ae50b", client_secret="b38b8057289c4d51a84f4b76d1981b58"))

while True:
    # Open music_catalogue_service.txt
    with open("music_catalogue_service.txt", "r") as f:
        music_catalogue_contents = f.read()

    # If the contents are not blank and do not equal the break key, search Spotify for the title and return
    if music_catalogue_contents != "":
        if music_catalogue_contents == BREAK_KEY:
            # Clear file contents and add break key before terminating program
            with open("music_catalogue_service.txt", "w"):
                pass
            with open("song_id.txt", "w") as f:
                f.write(BREAK_KEY)

            break

        results = spotify.search(music_catalogue_contents)
        song_url = results["tracks"]["items"][0]["id"]
        with open("song_id.txt", "w") as f:
            f.write(song_url)

        time.sleep(15)
        # Clear file contents
        with open("music_catalogue_service.txt", "w") as f:
            pass
