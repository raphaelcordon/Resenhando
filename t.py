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
        album_name1 = album_name
        album_name1 = str.replace(album_name1, "- ", "")
        for item in self.listAlbums:
            name = str.replace(item['name'], "- ", "")
            if album_name1 == name:
                return True

        album_name2 = album_name
        album_name2 = str.replace(album_name2, " (Deluxe Edition)", "")
        for item in self.listAlbums:
            name = str.replace(item['name'], " (Deluxe Edition)", "")
            if album_name2 == name:
                return True

        album_name3 = album_name
        album_name3 = str.replace(album_name3, " (Deluxe Version)", "")
        for item in self.listAlbums:
            name = str.replace(item['name'], " (Deluxe Version)", "")
            if album_name3 == name:
                return True

        album_name4 = album_name
        album_name4 = str.replace(album_name4, " (Expanded Edition)", "")
        for item in self.listAlbums:
            name = str.replace(item['name'], " (Expanded Edition)", "")
            if album_name4 == name:
                return True

        album_name5 = album_name
        album_name5 = str.replace(album_name5, " (Deluxe)", "")
        for item in self.listAlbums:
            name = str.replace(item['name'], " (Deluxe)", "")
            if album_name5 == name:
                return True

        album_name6 = album_name
        album_name6 = str.replace(album_name6, " (Remastered)", "")
        for item in self.listAlbums:
            name = str.replace(item['name'], " (Remastered)", "")
            if album_name6 == name:
                return True

        return False

get = SpotifyGetAlbums('7AC976RDJzL2asmZuz7qil')
for g in get.listAlbums:
    print(g)


class SpotifyGetFiveArtists:
    def __init__(self, name):
        """
        SpotifyGetFiveArtists returns the five first artists accordingly the user's search
        :param name: User's search object
        """
        self.name = name
        self.listArtists = []
        self.createList()

    def createList(self):
        print(SPOTIFY.search(q='artist:' + self.name, type='artist'))
        for list in SPOTIFY.search(q='artist:' + self.name, type='artist')['artists']['items'][:5]:
            image = list['images'][0]['url'] if len(list['images']) > 0 else ''
            if image != '':
                artist = {'id':     list['id'],
                          'name':   list['name'],
                          'image':  image,
                          'uri':    list['uri'],
                          'genres': list['genres']
                          }
                self.listArtists.append(artist)
        return self.listArtists


get = SpotifyGetFiveArtists('5')
for g in get.listArtists:
    print(g)
