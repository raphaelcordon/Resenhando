import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = '458d767d30034a44828d668093119d4f'
CLIENT_SECRET = '94362b7769f64dd298ae57852647527b'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
        client_id=CLIENT_ID, client_secret=CLIENT_SECRET))


class getFiveArtists:
    def __init__(self):
        self.listArtists = []
        self.createList()

    def createList(self):
        for list in spotify.search(q='artist:' + 'marisa monte', type='artist')['artists']['items'][:5]:
            artist = {'id':     list['id'],
                      'name':   list['name'],
                      'image': list['images'][0]['url'],
                      'uri':    list['uri'],
                      'genres': list['genres']
                      }
            self.listArtists.append(artist)
        return self.listArtists

print(spotify.search(q='artist:' + 'marisa monte', type='artist')['artists']['items'][:5])

"""
class getTopSix:
    def __init__(self, name='marisa monte'):
        lz_uri = spotify.search(q='artist:' + name, type='artist')
        self.artistId = []
        for count in range(0, 5):
            for count in lz_uri['artists']['items']:
                self.artistId.append(count['id'])
        self.trackPerArtist = {}
        self.listTopSix = []
        self.createList()

    def createList(self):
        for count in range(0, 5):
            for track in spotify.artist_top_tracks(self.artistId[count])['tracks'][:6]:
                tracks = {'name': track['name'],
                          'preview_url': track['preview_url'],
                          'image': track['album']['images'][0]['url']}
                self.listTopSix.append(tracks)
            self.trackPerArtist = {'artistID' : (self.listTopSix)}
        return self.trackPerArtist

"""
get = getFiveArtists()
for g in get.listArtists:
    print(g)

#topsix = getTopSix().listTopSix
#for g in topsix:
#    print(g)
