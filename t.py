import spotipy
import base64
import urllib
import argparse
import logging
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = '458d767d30034a44828d668093119d4f'
CLIENT_SECRET = '94362b7769f64dd298ae57852647527b'

SPOTIFY = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

logger = logging.getLogger('examples.artist_albums')
logging.basicConfig(level='INFO')


class SpotifyGetAlbums:
    def __init__(self, artistId):
        self.artistId = artistId
        self.albums = []
        self.listAlbums = []
        self.createList()

    def createList(self):
        results = SPOTIFY.artist_albums(self.artistId, album_type='album')
        self.albums.extend(results['items'])
        while results['next']:
            results = SPOTIFY.next(results)
            self.albums.extend(results['items'])

        seen = set()  # to avoid dups
        for self.item in self.albums:  # Clean list to send to the website
            if self.item['name'] not in seen:
                image = self.item['images'][0]['url'] if len(self.item['images']) > 0 else ''
                artist_name = self.item['artists'][0]['name'] if len(
                    self.item['artists']) > 0 else ''
                album_name = self.item['name']

                album = {'id': self.item['id'],
                         'name': self.item['name'],
                         'image': image,
                         'artist_name': artist_name,
                         'uri': self.item['uri'],
                         'release_date': self.item['release_date'][:4]
                         }

                if not self.__contains(album_name):
                    self.listAlbums.append(album)

        return self.listAlbums

    def __contains(self, album_name):
        album_name = str.replace(album_name, "- ", "")
        for item in self.listAlbums:
            name = str.replace(item['name'], "- ", "")
            if album_name == name:
                return True
        return False

get = SpotifyGetAlbums('6mdiAmATAx73kdxrNrnlao')
for g in get.listAlbums:
    print(g)

class SpotifyGetFiveArtists:
    def __init__(self, name):
        """
        Returns the five first artists accordingly the user's search
        :param name: User's search object
        """
        self.name = name
        self.listArtists = []
        self.createList()

    def createList(self):
        for list in SPOTIFY.search(q='artist:' + self.name, type='artist')['artists']['items'][:5]:
            image = list['images'][0]['url'] if len(list['images']) > 0 else ''
            artist = {'id':     list['id'],
                      'name':   list['name'],
                      'image':  image,
                      'uri':    list['uri'],
                      'genres': list['genres']
                      }
            self.listArtists.append(artist)
        return self.listArtists

get = SpotifyGetFiveArtists('Lenine')
for g in get.listArtists:
    print(g)
