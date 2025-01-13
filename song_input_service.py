import json
import os
import time


def homepage():
    print(""
          "███╗   ███╗██╗   ██╗███████╗██╗ ██████╗\n"
          "████╗ ████║██║   ██║██╔════╝██║██╔════╝\n"
          "██╔████╔██║██║   ██║███████╗██║██║     \n"
          "██║╚██╔╝██║██║   ██║╚════██║██║██║     \n"
          "██║ ╚═╝ ██║╚██████╔╝███████║██║╚██████╗\n"
          "╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝\n"
          "██████╗  █████╗ ████████╗ █████╗\n"
          "██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗\n"
          "██║  ██║███████║   ██║   ███████║\n"
          "██║  ██║██╔══██║   ██║   ██╔══██║\n"
          "██████╔╝██║  ██║   ██║   ██║  ██║\n"
          "╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝\n"
          " ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗\n"
          "██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗\n"
          "██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝\n"
          "██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗\n"
          "╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║\n"
          " ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝\n")

    user_answer = input("Welcome to the Music Recommendations Generator! "
                        "Would you like to see the app's functionality? Enter 'y' to view: ").lower()
    if user_answer == "y":
        print("\nApp Functionality:\n"
              "This app receives your song and returns a list of ten similar songs back to you.\n"
              "No costs involved, just type in your favorite song down below!")
    print()


def retrieve_song_data():
    """Retrieve song recommendations and clear file contents after."""
    try:
        with open("song_data.json", "r") as file:
            contents = json.load(file)

            time.sleep(5)
            with open("song_data.json", "w"):
                pass

            data = {
                "album_type": contents["album"]["album_type"],
                "album_name": contents["album"]["name"],
                "spotify_link": contents["external_urls"]["spotify"],
                "album_release_date": contents["album"]["release_date"],
                "name": contents["name"]
            }

            # Add song duration in minutes and seconds
            ms = contents["duration_ms"]
            seconds, ms = divmod(ms, 1000)
            minutes, seconds = divmod(seconds, 60)
            data["song_duration"] = f'{int(minutes):01d}:{int(seconds):02d}'

            # Add string containing all artists
            artists_data = contents["artists"]
            artists_array = [artist["name"] for artist in artists_data]
            all_artists = ", ".join(artists_array)
            data["artists"] = all_artists

            return data
    except json.JSONDecodeError:
        return False


homepage()
while True:
    # Get user input
    user_input = input("Enter a song 🔍: ")
    with open("music_catalogue_service.txt", "w") as f:
        f.write(user_input)

    # Retrieve recommendations
    song_data = retrieve_song_data()
    while song_data is False:
        song_data = retrieve_song_data()

    # Print recommendations
    print("\n----------------------------")
    print(
        f"\033[1mSong Data for '{user_input.title()}':\033[0m\n"
        f"Song name: {song_data["name"]}\n"
        f"Artists: {song_data["artists"]}\n"
        f"Album Release Date (yyyy-mm-dd): {song_data["album_release_date"]}\n"
        f"Spotify Link: {song_data["spotify_link"]}\n"
        f"From Album Type: {song_data["album_type"]}\n"
        f"Album Name: {song_data["album_name"]}\n"
        f"Song Duration: {song_data["song_duration"]}\n"
    )

    print("----------------------------\n")

    # Ask user to enter feedback
    if input("Would you like to provide any feedback for this program? Enter 'y' to enter feedback: ") == "y":
        feedback = input("Enter feedback: ")
        with open("user_feedback.txt", "w") as f:
            f.write(feedback)

    # Ask user if they would like to enter another song or quit the program
    if input("Would you like to enter another song? Enter 'y' to enter another song or "
             "another key to exit the program: ") != 'y':
        exit_or_no = input("Are you sure? Enter 'y' or 'i am sure.' to exit program: ").lower()
        if exit_or_no == "y" or exit_or_no == "i am sure.":
            print("\nSure, thanks for using our service! See you later!")

            # End music_catalogue service as well
            with open("music_catalogue_service.txt", "w") as f:
                f.write("SFG8YG0AUHvn0d8qygk3fhao81111111111")

            break

    # Ask user if they would like to go back to homepage
    homepage_or_no = input("Would you like to go back to the homepage? "
                           "Enter 'y' to go back: ")

    # Clear Python screen
    os.system("clear")

    if homepage_or_no == "y":
        homepage()
