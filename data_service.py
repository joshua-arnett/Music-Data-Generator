import json
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

BREAK_KEY = "SFG8YG0AUHvn0d8qygk3fhao81111111111"

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id="7822b25bde0c45ab8d566b23d88ae50b", client_secret="b38b8057289c4d51a84f4b76d1981b58"))

# File paths
input_file = "song_id.txt"  # Input file
output_file = "song_data.json"  # Output file


def listen_for_song_id():
    """
    Continuously listens for a song ID in song_id.txt, processes it,
    and appends recommendations to song_data.json.
    """
    while True:
        with open(input_file, "r") as f:
            song_url = f.read()

            if song_url == BREAK_KEY:  # Clear input file and terminate program if break key
                with open(input_file, "w"):
                    pass
                break

        if song_url:
            # Dump recommendations to output file
            track = spotify.track(track_id=song_url)
            # recommendations = spotify.search(genre=tracks["genre"])
            with open(output_file, "w") as f:
                json.dump(track, f)
            #
            time.sleep(25)
            # Clear input file
            with open(input_file, "w"):
                pass


if __name__ == "__main__":
    listen_for_song_id()
