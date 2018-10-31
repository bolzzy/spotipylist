#/usr/bin/env python3

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import configparser


def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s %s" % (i, track['artists'][0]['name'],
            track['name'], track['uri']))


def get_song_ids(tracks):
    songids=[]
    for i, item in enumerate(tracks['items']):
        track = item['track']
        songids.append(track['id'])

    return songids

config = configparser.ConfigParser()
config.read("config.txt")

cid = config.get("app","clientid")
secret = config.get("app","clientsecret")
username = config.get("userspesific","username")
new_playlist = config.get("userspesific","newreleasesplaylist")
release_radar = config.get("userspesific","release_radar")


client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-library-read playlist-read-private playlist-modify-private'
token = util.prompt_for_user_token(username, scope, cid, secret, "http://localhost:1339/callback")

try:
    sp = spotipy.Spotify(auth=token)
except:
    print("Can't get token for", username)
    exit()


radarsongs = sp.user_playlist(username,release_radar,fields="tracks")
rtracks = radarsongs['tracks']
rsongids = get_song_ids(rtracks)

newsongs = sp.user_playlist(username,new_playlist,fields="tracks")
ntracks = newsongs['tracks']
nsongids = get_song_ids(ntracks)


addsongs=[]

for song in rsongids:
    if song in nsongids:
        print("duplicate: " + song)
    else:
        addsongs.append(song)

if addsongs:
    result = sp.user_playlist_add_tracks(username,new_playlist,addsongs)
    print(result)
