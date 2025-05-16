from ytmusicapi import YTMusic, OAuthCredentials
import os
import dotenv
import shutil

# Load environment variables from .env file
dotenv.load_dotenv()

client_id = dotenv.get_key(dotenv.find_dotenv(), "CLIENT_ID")
client_secret = dotenv.get_key(dotenv.find_dotenv(), "CLIENT_SECRET")

# Initialize YTMusic with OAuth credentials
ytm = YTMusic('oauth.json', oauth_credentials=OAuthCredentials(client_id, client_secret))

# Ask the user for the playlist ID
playlist_id = input("Enter the playlist ID: ")

# Create a directory for the playlist
def create_directory(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print(f"Directory '{dir_name}' created.")
    else:
        print(f"Directory '{dir_name}' already exists.")

def download_playlist(playlist_id):
    # Get the playlist details
    playlist = ytm.get_playlist(playlist_id)
    print(f"Playlist Title: {playlist['title']}")
    print(f"Playlist ID: {playlist['id']}")
    print(f"Playlist Description: {playlist['description']}")

    # Create a directory for the playlist
    if ' ' in playlist['title']:
        playlist['title'] = playlist['title'].replace(' ', '_')
    create_directory(dir_name=playlist['title'])

    # Download each song in the playlist
    for song in playlist['tracks']:
        song_title = song['title']
        song_id = song['videoId']
        song_artist = song['artists'][0]['name']
        file_name = song_artist + " - " + song_title + ".mp3"
        print("Downloading: ", song_title)

        # Check if the song is already downloaded
        if os.path.exists(os.path.join(playlist['title'], song_title + ".mp3")):
            print(f"'{song_title}' already downloaded.")

        if os.path.exists(file_name) or os.path.exists(playlist['title'] + "/" + file_name):
            print(f"'{file_name}' already exists in the current directory or playlist directory.")
            continue
            
        # Download the song using yt-dlp        
        else:
            command = f'yt-dlp -x --audio-format mp3 --output "{file_name}" {song_id}'
            os.system(command)

       
        shutil.move(file_name, playlist['title'])
        print(f"'{file_name}' moved to '{playlist['title']}' directory.")
        

    print("All songs downloaded successfully!")


# Main function
if __name__ == "__main__":
    download_playlist(playlist_id)