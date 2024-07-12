import os

def delete_downloaded_files():
    # Directory containing downloaded songs
    download_dir = "downloaded_songs"
    
    # Path to the file listing downloaded songs
    downloaded_songs_file = os.path.join(download_dir, "downloaded_songs.txt")
    
    # Check if the file exists
    if not os.path.exists(downloaded_songs_file):
        print("No downloaded songs file found.")
        return
    
    # Read the file and delete each listed song
    with open(downloaded_songs_file, 'r') as f:
        downloaded_songs = f.read().splitlines()
    
    for song in downloaded_songs:
        song_path = os.path.join(download_dir, f"{song}.mp3")
        if os.path.exists(song_path):
            try:
                os.remove(song_path)
                print(f"Deleted {song_path}")
            except Exception as e:
                print(f"Failed to delete {song_path}: {e}")
        else:
            print(f"File {song_path} does not exist.")
    
    # Delete the downloaded_songs.txt file
    try:
        os.remove(downloaded_songs_file)
        print(f"Deleted {downloaded_songs_file}")
    except Exception as e:
        print(f"Failed to delete {downloaded_songs_file}: {e}")

if __name__ == "__main__":
    delete_downloaded_files()
