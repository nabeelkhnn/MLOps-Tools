import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

def run_spotify_etl():
    client_id = "177294fedbe24a64b2ebd2d019eba74a"  # Your Spotify API client ID
    client_secret = "001b4786a58b433fa94fb86a06a69b27"  # Your Spotify API client secret

    # Spotify authentication
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Fetch tracks from a playlist or user's saved tracks
    results = sp.playlist_tracks(playlist_id='6UeSakyzhiEt4NB3UAd6NQ')  # Use the extracted playlist_id


    tracks_list = []
    for track in results['items']:
        # Assuming we're working with track data, we could extract the following
        track_info = {
            'artist': track['track']['artists'][0]['name'],
            'album': track['track']['album']['name'],
            'track_name': track['track']['name'],
            'release_date': track['track']['album']['release_date'],
            'duration_ms': track['track']['duration_ms'],
            'popularity': track['track']['popularity']
        }
        
        tracks_list.append(track_info)

    # Convert the extracted track data into a pandas DataFrame
    df = pd.DataFrame(tracks_list)
    
    # Save the DataFrame to a CSV file
    df.to_csv('spotify_tracks_data.csv')

# Run the ETL process
run_spotify_etl()
