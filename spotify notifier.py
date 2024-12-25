import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time

# Set your Spotify Developer credentials
SPOTIFY_CLIENT_ID = "2b9a7b9c514c4a4db935d9b1c2f21f44"
SPOTIFY_CLIENT_SECRET = "a7c4be142f784637b591602c66cb30e1"

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_latest_song(artist_name):
    # Search for the artist
    results = sp.search(q=f"artist:{artist_name}", type="artist")
    if not results['artists']['items']:
        print(f"No artist found with the name {artist_name}")
        return None
    
    artist_id = results['artists']['items'][0]['id']
    
    # Get the artist's albums
    albums = sp.artist_albums(artist_id, album_type='single', limit=1)
    if not albums['items']:
        print(f"No singles found for {artist_name}")
        return None

    latest_song = albums['items'][0]
    return {
        'name': latest_song['name'],
        'release_date': latest_song['release_date'],
        'url': latest_song['external_urls']['spotify']
    }

def main():
    artist_name = input("Enter the name of the artist: ")
    print("Fetching latest song...")
    
    while True:
        try:
            latest_song = get_latest_song(artist_name)
            if latest_song:
                print(f"Latest song: {latest_song['name']}")
                print(f"Release date: {latest_song['release_date']}")
                print(f"Listen on Spotify: {latest_song['url']}")
            else:
                print("No latest song found.")
            
            # Check for updates every hour
            time.sleep(3600)
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    main()
