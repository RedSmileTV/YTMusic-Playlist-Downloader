from ytmusicapi import YTMusic, OAuthCredentials
import os
import dotenv
import shutil

# Load environment variables
dotenv.load_dotenv()
client_id = dotenv.get_key(dotenv.find_dotenv(), "CLIENT_ID")
client_secret = dotenv.get_key(dotenv.find_dotenv(), "CLIENT_SECRET")

# Initialize YTMusic
ytm = YTMusic('oauth.json', oauth_credentials=OAuthCredentials(client_id, client_secret))

def get_user_input():
    playlist_id = input("Enter the playlist ID: ").strip()
    file_ext = input("Enter the file extension [mp3, m4a, wav] (default: mp3): ").strip().lower()
    return playlist_id, file_ext if file_ext in {"mp3", "m4a", "wav"} else "mp3"

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")
    else:
        print(f"Directory already exists: {path}")

def sanitize_filename(name):
    for char in ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '#']:
        name = name.replace(char, '')
    return name.strip()

def download_song(song, file_ext, output_dir):
    title = song['title']
    artist = song['artists'][0]['name']
    video_id = song['videoId']
    file_name = sanitize_filename(f"{artist} - {title}")
    file_path = os.path.join(output_dir, f"{file_name}.{file_ext}")

    if os.path.exists(file_path):
        print(f"'{file_name}' already exists. Skipping...")
        return

    ytdlp_cmd = (
        f'yt-dlp --embed-thumbnail --embed-metadata -x --audio-format "{file_ext}" '
        f'--output "{file_name}.%(ext)s" {video_id}'
    )
    if file_ext == "wav":
        ytdlp_cmd = ytdlp_cmd.replace('--embed-thumbnail ', '')  # WAV doesn't support thumbnails

    print(f"Downloading: {title}")
    try:
        os.system(ytdlp_cmd)
        downloaded_file = f"{file_name}.{file_ext}"
        shutil.move(downloaded_file, output_dir)
        print(f"Moved '{downloaded_file}' to '{output_dir}'.")
    except Exception as e:
        print(f"Error downloading or moving '{file_name}': {e}")

def download_playlist(playlist_id, file_ext):
    playlist = ytm.get_playlist(playlist_id)
    title = sanitize_filename(playlist['title'])
    print(f"\nPlaylist: {playlist['title']}\nDescription: {playlist['description']}")
    create_directory(title)

    for track in playlist['tracks']:
        download_song(track, file_ext, title)

    print("\nDownload complete!")

# Main logic
if __name__ == "__main__":
    playlist_id, file_extension = get_user_input()
    download_playlist(playlist_id, file_extension)
