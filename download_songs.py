import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import yt_dlp as youtube_dl

# Set your Spotify API credentials
SPOTIPY_CLIENT_ID = '3315f701d23a425a9dc412eac4fe6b98'
SPOTIPY_CLIENT_SECRET = 'f858197fd39d4135a3aab4f609f39359'
SPOTIPY_REDIRECT_URI = 'http://localhost:8000/callback'

# Path to the cache file
CACHE_FILE = ".cache"

# Check if the cache file exists and remove it
if os.path.exists(CACHE_FILE):
    os.remove(CACHE_FILE)
    print(f"Deleted cached token file: {CACHE_FILE}")

# Authenticate with Spotify
def authenticate_spotify():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                     client_secret=SPOTIPY_CLIENT_SECRET,
                                                     redirect_uri=SPOTIPY_REDIRECT_URI,
                                                     scope="user-library-read",
                                                     cache_path=CACHE_FILE))

# Fetch liked songs from Spotify
def fetch_liked_songs(sp, offset=0, limit=50):
    songs = []
    results = sp.current_user_saved_tracks(limit=limit, offset=offset)
    for item in results['items']:
        song_name = item['track']['name']
        artist_name = item['track']['artists'][0]['name']
        songs.append(f"{song_name} {artist_name}")
    return songs

# Function to download MP3 using yt-dlp
def download_song(song):
    search_url = f"ytsearch:{song}"
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'downloaded_songs/{song}.mp3',
        'ffmpeg_location': 'C:\\ffmpeg-master-latest-win64-gpl\\bin',  # Add this line to specify the location of ffmpeg
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([search_url])
    except Exception as e:
        print(f"Failed to download {song}: {e}")

# Load offset from file
def load_offset(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return int(f.read().strip())
    return 0

# Save offset to file
def save_offset(file_path, offset):
    with open(file_path, 'w') as f:
        f.write(str(offset))

# Main function
def main():
    sp = authenticate_spotify()
    offset_file = "offset.txt"
    offset = load_offset(offset_file)
    
    # Fetch 50 liked songs from the current offset
    songs = fetch_liked_songs(sp, offset=offset, limit=50)

    if not songs:
        print("No new songs to download.")
        return

    # Directory to save downloaded songs
    download_dir = "downloaded_songs"
    os.makedirs(download_dir, exist_ok=True)

    # Keep track of downloaded songs
    downloaded_songs_file = os.path.join(download_dir, "downloaded_songs.txt")
    if not os.path.exists(downloaded_songs_file):
        with open(downloaded_songs_file, 'w') as f:
            pass

    # Load previously downloaded songs
    with open(downloaded_songs_file, 'r') as f:
        downloaded_songs = f.read().splitlines()

    # Filter out already downloaded songs
    new_songs = [song for song in songs if song not in downloaded_songs]

    if not new_songs:
        print("No new songs to download.")
        return

    # Download new songs and update the downloaded songs list
    with open(downloaded_songs_file, 'a') as f:
        for song in new_songs:
            download_song(song)
            f.write(f"{song}\n")

    # Update offset for the next batch
    offset += 50
    save_offset(offset_file, offset)

if __name__ == "__main__":
    main()
