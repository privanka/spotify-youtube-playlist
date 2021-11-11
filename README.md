# Youtube to Spotify Playlist

Python script that takes liked videos on Youtube account, and generates a Spotify playlist with songs in your liked videos list.

## Local Setup Instructions

1. Install dependencies using: `pip3 install -r requirements.txt`<br><br>
2. Get your Spotify ID and Oauth Token using the Developers for Spotify [site](https://developer.spotify.com/console/post-playlists/).
    * To get Spotify ID, login to Spotify and visit the Account Overview [tab](https://www.spotify.com/us/account/overview/) to collect your username.
    * To get Oauth token, visit this [link](https://developer.spotify.com/console/post-playlists/), and click the "Get Token" button. <br><br> 

3. Set up Oauth on Youtube account and download client_secret.json file. 
    * Follow the instructions on the Youtube Data API Overview [site](https://developers.google.com/youtube/v3/getting-started).
    * Ensure that on the "Credentials" page, the YouTube Data API v3 status is set to "on" before setting up the Oauth Client ID, and obtaining the json file.
    * Make to sure to enable Oauth on the proper Google/Youtube account you want to link for this project. <br><br>

4. Run program file: `python3 create_playlist.py`
   * If the program runs without any errors, the console will print: <br>
     ```
     Please visit this URL to authorize this application: [link to sign in to Google acct]

     Enter the authorization code:
     ```
   * Sign into your Google account to get the authorization code, and enter it to your terminal.
   * If the program runs successfully, the shell should return: `Response gave status code 201` <br><br>
   * For troubleshooting purposes, Spotify tokens expire quickly and if you run into a `KeyError` this could be due to an expired token. At which point you will need to get a new token, and replace the old token in your secrets file.

#### Technologies Used:

* [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
* [Youtube Data API](https://developers.google.com/youtube/v3/getting-started)
* [Youtube DL](https://github.com/ytdl-org/youtube-dl)
