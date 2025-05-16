# YTMusicDownloader

A simple script to download music from YouTube.

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/YTMusicDownloader.git
    cd YTMusicDownloader
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    # On Windows:

    # Powershell
    venv\Scripts\Activate.ps1
    
    # CMD
    venv\Scripts\activate.bat

    # On macOS/Linux:
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Create your Credentials**
    follow [this](https://ytmusicapi.readthedocs.io/en/latest/setup/oauth.html) guide for setting up the YouTubeAPI

5. **Create and Fill out a .env file in the same directory:**

    **Example .env file**
    ```
    CLIENT_ID=YOUR_CLIENT_ID
    CLIENT_SECRET=YOUR_CLIENT_SECRET
    ```

    **Once you got your credentials in your .env file and oauth.json in the working directory
    you can run the script**


## Usage

1. **Run the script:**
    ```sh
    python main.py
    ```

2. **Follow the prompts** enter the playlist ID of the Youtube / Youtube Music playlist you want to download  

## Notes

- A Folder with the playlist name will be created in the current directory
- Any spaces in the playlist name will be replaced by "_"
