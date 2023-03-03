import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

#spotify stuff that lets me do things with the app 
SPOTIFY_CLIENT_ID = "ed6fe433e91b43a79490bea46ef85b00"
SPOTIFY_SECRET = "4b2a58733e6a40c4b221d44d83f9d81a"
REDIRECT_URL = "http://localhost:8000"
scope="app-remote-control user-modify-playback-state",

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

devices = spotify.devices()
device_id = devices['devices'][0]['id']

print(spotify.devices())

# track_uri = "spotify:track:4R67rQNSbbsR4TdUVOIdez"
# sp.add_to_queue(track_uri)
# sp.start_playback()
