# Spotify Liked Songs Downloader

This project allows users to fetch their liked songs from Spotify and download them as MP3 files using `yt-dlp`. It utilizes the Spotify Web API for fetching liked songs and `yt-dlp` for downloading the songs from YouTube.

## Features

- Authenticate with Spotify and fetch liked songs.
- Download songs as MP3 files using `yt-dlp`.
- Maintain a record of downloaded songs to avoid duplicates.
- Resume downloads from the last processed song using an offset.

## Prerequisites

- Python 3.x
- `spotipy` library
- `yt-dlp` library
- `ffmpeg` installed and configured in your PATH

## Setup

1. **Clone the repository:**
    
    ```bash
    git clone <https://github.com/your-username/spotify-liked-songs-downloader.git>
    cd spotify-liked-songs-downloader
    
    ```
    
2. **Install required libraries:**
    
    ```bash
    pip install spotipy yt-dlp
    
    ```
    
3. **Download and configure `ffmpeg`:**
    - Download `ffmpeg` from [ffmpeg.org](https://ffmpeg.org/download.html).
    - Extract the files and place them in a known location.
    - Add the `bin` folder to your system's PATH environment variable.
4. **Set up Spotify Developer Credentials:**
    - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
    - Create a new application.
    - Add `http://localhost:8000/callback` as a Redirect URI in the application settings.
    - Note down your `Client ID`, `Client Secret`, and `Redirect URI`.
5. **Update the credentials in the script:**
    
    ```python
    SPOTIPY_CLIENT_ID = 'your-client-id'
    SPOTIPY_CLIENT_SECRET = 'your-client-secret'
    SPOTIPY_REDIRECT_URI = '<http://localhost:8000/callback>'
    
    ```
    

## Usage

1. **Run the script:**
    
    ```bash
    python main.py
    
    ```
    
2. **Authenticate with Spotify:**
    - A web browser will open for Spotify authentication.
    - Login and authorize the application.
3. **Download songs:**
    - The script will fetch your liked songs from Spotify and download them as MP3 files.
    - The downloaded songs will be saved in the `downloaded_songs` directory.

## Script Details

### Authentication

The script uses `spotipy.Spotify` with `SpotifyOAuth` to authenticate with Spotify and obtain access tokens. The tokens are cached in a file named `.cache`.

### Fetching Liked Songs

The `fetch_liked_songs` function fetches liked songs from Spotify in batches of 50. It extracts the song name and artist name for each song.

### Downloading Songs

The `download_song` function uses `yt-dlp` to search for the song on YouTube and download it as an MP3 file. It specifies the `ffmpeg` location to ensure the downloaded file is converted to MP3 format.

### Maintaining State

The script keeps track of the songs downloaded and the offset (i.e., the position in the liked songs list) to resume downloading from where it left off. The offset is saved in a file named `offset.txt`, and the downloaded songs are recorded in `downloaded_songs.txt`.

## Error Handling

The script includes basic error handling to manage issues that might arise during the download process, such as failed downloads.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgements

- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [spotipy](https://spotipy.readthedocs.io/)
