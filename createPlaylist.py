'''
Steps overview
1. Youtube login/credentials
2. Grab Liked videos
3. Create a new playlist on spotify
4. Search for song
5. Add song to new spotify playlist
'''

'''
Youtube Data API
Spotify Web API
Youtube DL library
'''

import json
import requests
from secrets import spotify_user_id

class createPlaylist:

    def __init__(self) -> None:
        pass
        self.user_id = spotify_user_id

    def get_youtube_client(self):
        pass

    def get_liked_videos(self):
        pass

    def create_spotify_playlist(self):
        pass

        '''
        get spotify username and OAuth token and store as a secret
        gives: endpoint, HTTP method
        '''

        request_body = json.dumps{{
            "name": "Songs Found on Youtube",
            "description": "All liked youtube vids",
            "public": True
        }}
        


    def get_spotify_url(self):
        pass

    def add_song_to_playlist(self):
        pass