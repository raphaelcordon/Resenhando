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


class getAlbuns:
    def __init__(self):
        self.listAlbums = []
        self.createList()

    def createList(self):
        for albumList in SPOTIFY.artist_albums('6mdiAmATAx73kdxrNrnlao', limit=50)['items']:
            try:
                checkRegisters = list(map(itemgetter(albumList['name']), self.listAlbums))
                print(checkRegisters)
            except:
                pass
            if albumList['album_group'] == 'album':
                image = albumList['images'][0]['url'] if len(albumList['images']) > 0 else ''
                artist_name = albumList['artists'][0]['name'] if len(albumList['artists']) > 0 else ''
                album_name = albumList['name']

                album = {'id': albumList['id'],
                         'album_name': album_name,
                         'image': image,
                         'artist_name': artist_name,
                         'uri': albumList['uri'],
                         'release_date': albumList['release_date'][:4]
                         }

                if not self.__contains(album_name):
                    self.listAlbums.append(album)

        return self.listAlbums
    
    def __contains(self, album_name):
        for item in self.listAlbums:
            album_name = str.replace(album_name, "- ", "")
            _album_name = str.replace(item["album_name"], "- ", "")
            if _album_name == album_name:
                return True
        return False 


get = getAlbuns()
for g in get.listAlbums:
    print(g)


"""
class getFiveArtists:
    def __init__(self):
        self.listArtists = []
        self.createList()

    def createList(self):
        for list in spotify.search(q='artist:' + 'type', type='artist')['artists']['items'][:5]:
            image = list['images'][0]['url'] if len(list['images']) > 0 else ''
            artist = {'id':     list['id'],
                      'name':   list['name'],
                      'image':  list['images'],
                      'uri':    list['uri'],
                      'genres': list['genres']
                      }
            self.listArtists.append(artist)
        return self.listArtists


get = getFiveArtists()
for g in get.listArtists:
    print(g)
"""


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
        for self.sortingAlbum in self.albums:  # Clean list to send to the website
            if self.sortingAlbum['name'] not in seen:
                if CheckDuplicatedVersions(self.sortingAlbum) not in seen:
                    seen.add(self.sortingAlbum['name'])

                    image = self.sortingAlbum['images'][0]['url'] if len(self.sortingAlbum['images']) > 0 else ''
                    artist_name = self.sortingAlbum['artists'][0]['name'] if len(self.sortingAlbum['artists']) > 0 else ''
                    album = {'id': self.sortingAlbum['id'],
                             'name': self.sortingAlbum['name'],
                             'image': image,
                             'artist_name': artist_name,
                             'uri': self.sortingAlbum['uri'],
                             'release_date': self.sortingAlbum['release_date'][:4]
                             }
                    self.listAlbums.append(album)
                else:
                    print(CheckDuplicatedVersions(self.sortingAlbum))


def CheckDuplicatedVersions(album):
    duplicated = ''
    items = [' Remixed', ' (Special Edition)', ' (Remastered)',
             ' (Remastered Edition)', ' (Expanded Edition)',
             ' (Deluxe)', ' [Deluxe]', 'Remaster']
    itemsWithYear = [' Remastered)', ' Remixed)', ' Remasterizado)', ' Remixado)', ' Remaster)', ' - Remaster)']
    for item in items:
        if item in str(album).lower():
            check = album.lower().find(item)
            duplicated = item[0:check]
    for item in itemsWithYear:
        if (item in str(album).lower()):
            check = album.lower().find(item)
            duplicated = item[0:(check -6)]
    if duplicated != '':
        return duplicated


get = SpotifyGetAlbums('6mdiAmATAx73kdxrNrnlao')
for g in get.listAlbums:
    print(g)





# com ano:
' (xxxx Remastered)', ' (xxxx Remixed)',' (xxxx Remasterizado)', ' (xxxx Remixado)'


"""
if albumList['album_group'] == 'album':
    image = albumList['images'][0]['url'] if len(albumList['images']) > 0 else ''
    artist_name = albumList['artists'][0]['name'] if len(albumList['artists']) > 0 else ''
    album = {'id': albumList['id'],
             'name': albumList['name'],
             'image': image,
             'artist_name': artist_name,
             'uri': albumList['uri'],
             'release_date': albumList['release_date'][:4]
             }
    self.listAlbums.append(album)
return self.listAlbums
"""




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



topsix = getTopSix().listTopSix
for g in topsix:
    print(g)

"""
"""
[   {'album_group': 'album', 'album_type': 'album', '
    artists': [{
    'external_urls': {'spotify': 'https://open.spotify.com/artist/0blJzvevdXrp21YeI2vbco'}, 
    'href': 'https://api.spotify.com/v1/artists/0blJzvevdXrp21YeI2vbco', 
    'id': '0blJzvevdXrp21YeI2vbco', 
    'name': 'Type O Negative', 'type': 'artist', 'uri': 'spotify:artist:0blJzvevdXrp21YeI2vbco'}], 
    
    
    'available_markets': [], 
    'external_urls': {'spotify': 'https://open.spotify.com/album/5LtfWD1Iby98F4k2WPgWeV'}, 
    'href': 'https://api.spotify.com/v1/albums/5LtfWD1Iby98F4k2WPgWeV', 
    'id': '5LtfWD1Iby98F4k2WPgWeV', 
    'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273011edac5965fb29c2918e1af', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02011edac5965fb29c2918e1af', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851011edac5965fb29c2918e1af', 'width': 64}], 
    'name': 'The Complete Roadrunner Collection 1991-2003', 
    'release_date': '2013', 
    'release_date_precision': 'year', 
    'total_tracks': 71, 
    'type': 'album', 
    'uri': 'spotify:album:5LtfWD1Iby98F4k2WPgWeV'},
    
    {'album_group': 'album', 'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0blJzvevdXrp21YeI2vbco'}, 'href': 'https://api.spotify.com/v1/artists/0blJzvevdXrp21YeI2vbco', 'id': '0blJzvevdXrp21YeI2vbco', 'name': 'Type O Negative', 'type': 'artist', 'uri': 'spotify:artist:0blJzvevdXrp21YeI2vbco'}], 'available_markets': [], 'external_urls': {'spotify': 'https://open.spotify.com/album/4AdGr92Z6Ff2WbKP5Ja2QC'}, 'href': 'https://api.spotify.com/v1/albums/4AdGr92Z6Ff2WbKP5Ja2QC', 'id': '4AdGr92Z6Ff2WbKP5Ja2QC', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273d736b2c5f252f84ad45d5be6', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02d736b2c5f252f84ad45d5be6', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851d736b2c5f252f84ad45d5be6', 'width': 64}], 'name': 'Life Is Killing Me', 'release_date': '2003-06-09', 'release_date_precision': 'day', 'total_tracks': 15, 'type': 'album', 'uri': 'spotify:album:4AdGr92Z6Ff2WbKP5Ja2QC'},
    {'album_group': 'album', 'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0blJzvevdXrp21YeI2vbco'}, 'href': 'https://api.spotify.com/v1/artists/0blJzvevdXrp21YeI2vbco', 'id': '0blJzvevdXrp21YeI2vbco', 'name': 'Type O Negative', 'type': 'artist', 'uri': 'spotify:artist:0blJzvevdXrp21YeI2vbco'}], 'available_markets': [], 'external_urls': {'spotify': 'https://open.spotify.com/album/19GlIEIJqujc5U5B7PETZW'}, 'href': 'https://api.spotify.com/v1/albums/19GlIEIJqujc5U5B7PETZW', 'id': '19GlIEIJqujc5U5B7PETZW', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b27319dba8c09733c29f11d74a6a', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e0219dba8c09733c29f11d74a6a', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d0000485119dba8c09733c29f11d74a6a', 'width': 64}], 'name': 'World Coming Down', 'release_date': '1999-09-13', 'release_date_precision': 'day', 'total_tracks': 13, 'type': 'album', 'uri': 'spotify:album:19GlIEIJqujc5U5B7PETZW'},
    {'album_group': 'album', 'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0blJzvevdXrp21YeI2vbco'}, 'href': 'https://api.spotify.com/v1/artists/0blJzvevdXrp21YeI2vbco', 'id': '0blJzvevdXrp21YeI2vbco', 'name': 'Type O Negative', 'type': 'artist', 'uri': 'spotify:artist:0blJzvevdXrp21YeI2vbco'}], 'available_markets': [], 'external_urls': {'spotify': 'https://open.spotify.com/album/6BkeUWI72Lssc077AxqQek'}, 'href': 'https://api.spotify.com/v1/albums/6BkeUWI72Lssc077AxqQek', 'id': '6BkeUWI72Lssc077AxqQek', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273704dd95c3ea01a719da5d5d4', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02704dd95c3ea01a719da5d5d4', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851704dd95c3ea01a719da5d5d4', 'width': 64}], 'name': 'October Rust (Special Edition)', 'release_date': '1996-08-19', 'release_date_precision': 'day', 'total_tracks': 18, 'type': 'album', 'uri': 'spotify:album:6BkeUWI72Lssc077AxqQek'},
    {'album_group': 'album', 'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0blJzvevdXrp21YeI2vbco'}, 'href': 'https://api.spotify.com/v1/artists/0blJzvevdXrp21YeI2vbco', 'id': '0blJzvevdXrp21YeI2vbco', 'name': 'Type O Negative', 'type': 'artist', 'uri': 'spotify:artist:0blJzvevdXrp21YeI2vbco'}], 'available_markets': [], 'external_urls': {'spotify': 'https://open.spotify.com/album/46NjYrJ5v5ZTIHMb1DrAgl'}, 'href': 'https://api.spotify.com/v1/albums/46NjYrJ5v5ZTIHMb1DrAgl', 'id': '46NjYrJ5v5ZTIHMb1DrAgl', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273ff7871e35825b5aea95beff3', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02ff7871e35825b5aea95beff3', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851ff7871e35825b5aea95beff3', 'width': 64}], 'name': 'October Rust', 'release_date': '1996-08-19', 'release_date_precision': 'day', 'total_tracks': 15, 'type': 'album', 'uri': 'spotify:album:46NjYrJ5v5ZTIHMb1DrAgl'},
    {'album_group': 'album', 'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0blJzvevdXrp21YeI2vbco'}, 'href': 'https://api.spotify.com/v1/artists/0blJzvevdXrp21YeI2vbco', 'id': '0blJzvevdXrp21YeI2vbco', 'name': 'Type O Negative', 'type': 'artist', 'uri': 'spotify:artist:0blJzvevdXrp21YeI2vbco'}], 'available_markets': [], 'external_urls': {'spotify': 'https://open.spotify.com/album/127mCJhPsHAB33rOYybK04'}, 'href': 'https://api.spotify.com/v1/albums/127mCJhPsHAB33rOYybK04', 'id': '127mCJhPsHAB33rOYybK04', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b27326afc3f1635038a3a90da306', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e0226afc3f1635038a3a90da306', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d0000485126afc3f1635038a3a90da306', 'width': 64}], 'name': 'Bloody Kisses', 'release_date': '1993', 'release_date_precision': 'year', 'total_tracks': 14, 'type': 'album', 'uri': 'spotify:album:127mCJhPsHAB33rOYybK04'},
    {'album_group': 'album', 'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0blJzvevdXrp21YeI2vbco'}, 'href': 'https://api.spotify.com/v1/artists/0blJzvevdXrp21YeI2vbco', 'id': '0blJzvevdXrp21YeI2vbco', 'name': 'Type O Negative', 'type': 'artist', 'uri': 'spotify:artist:0blJzvevdXrp21YeI2vbco'}], 'available_markets': [], 'external_urls': {'spotify': 'https://open.spotify.com/album/22PP61GmfGKAhIQo2ZSRxG'}, 'href': 'https://api.spotify.com/v1/albums/22PP61GmfGKAhIQo2ZSRxG', 'id': '22PP61GmfGKAhIQo2ZSRxG', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273bf9eaa56ca46fd6d2b3800d1', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02bf9eaa56ca46fd6d2b3800d1', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851bf9eaa56ca46fd6d2b3800d1', 'width': 64}], 'name': 'Bloody Kisses (Top Shelf Edition)', 'release_date': '1993', 'release_date_precision': 'year', 'total_tracks': 17, 'type': 'album', 'uri': 'spotify:album:22PP61GmfGKAhIQo2ZSRxG'},
    {'album_group': 'album', 'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0blJzvevdXrp21YeI2vbco'}, 'href': 'https://api.spotify.com/v1/artists/0blJzvevdXrp21YeI2vbco', 'id': '0blJzvevdXrp21YeI2vbco', 'name': 'Type O Negative', 'type': 'artist', 'uri': 'spotify:artist:0blJzvevdXrp21YeI2vbco'}], 'available_markets': [], 'external_urls': {'spotify': 'https://open.spotify.com/album/1XugE3dbDDfPlqNoyZDaih'}, 'href': 'https://api.spotify.com/v1/albums/1XugE3dbDDfPlqNoyZDaih', 'id': '1XugE3dbDDfPlqNoyZDaih', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273a0692e802cf2964053ef3eee', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02a0692e802cf2964053ef3eee', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851a0692e802cf2964053ef3eee', 'width': 64}], 'name': 'The Origin of the Feces (2007 Reissue)', 'release_date': '1992', 'release_date_precision': 'year', 'total_tracks': 8, 'type': 'album', 'uri': 'spotify:album:1XugE3dbDDfPlqNoyZDaih'},
    {'album_group': 'album', 'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0blJzvevdXrp21YeI2vbco'}, 'href': 'https://api.spotify.com/v1/artists/0blJzvevdXrp21YeI2vbco', 'id': '0blJzvevdXrp21YeI2vbco', 'name': 'Type O Negative', 'type': 'artist', 'uri': 'spotify:artist:0blJzvevdXrp21YeI2vbco'}], 'available_markets': [], 'external_urls': {'spotify': 'https://open.spotify.com/album/38xbAsUXuymB2Tuo8F2u6A'}, 'href': 'https://api.spotify.com/v1/albums/38xbAsUXuymB2Tuo8F2u6A', 'id': '38xbAsUXuymB2Tuo8F2u6A', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b2733491fa9c28dd0174dc6a9d63', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e023491fa9c28dd0174dc6a9d63', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d000048513491fa9c28dd0174dc6a9d63', 'width': 64}], 'name': 'Slow, Deep and Hard (2009 Remaster)', 'release_date': '1991-06-03', 'release_date_precision': 'day', 'total_tracks': 8, 'type': 'album', 'uri': 'spotify:album:38xbAsUXuymB2Tuo8F2u6A'},
    {'album_group': 'album', 'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0blJzvevdXrp21YeI2vbco'}, 'href': 'https://api.spotify.com/v1/artists/0blJzvevdXrp21YeI2vbco', 'id': '0blJzvevdXrp21YeI2vbco', 'name': 'Type O Negative', 'type': 'artist', 'uri': 'spotify:artist:0blJzvevdXrp21YeI2vbco'}], 'available_markets': [], 'external_urls': {'spotify': 'https://open.spotify.com/album/5zrFsgcNNQs6K3RqGCSqvl'}, 'href': 'https://api.spotify.com/v1/albums/5zrFsgcNNQs6K3RqGCSqvl', 'id': '5zrFsgcNNQs6K3RqGCSqvl', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273054ac4c47dad3cfc43a4b50e', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02054ac4c47dad3cfc43a4b50e', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851054ac4c47dad3cfc43a4b50e', 'width': 64}], 'name': 'Slow, Deep and Hard', 'release_date': '1991-06-03', 'release_date_precision': 'day', 'total_tracks': 7, 'type': 'album', 'uri': 'spotify:album:5zrFsgcNNQs6K3RqGCSqvl'},
    {'album_group': 'compilation', 'album_type': 'compilation', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0blJzvevdXrp21YeI2vbco'}, 'href': 'https://api.spotify.com/v1/artists/0blJzvevdXrp21YeI2vbco', 'id': '0blJzvevdXrp21YeI2vbco', 'name': 'Type O Negative', 'type': 'artist', 'uri': 'spotify:artist:0blJzvevdXrp21YeI2vbco'}], 'available_markets': [], 'external_urls': {'spotify': 'https://open.spotify.com/album/3D5JoPheRL85pJEg4gZC3G'}, 'href': 'https://api.spotify.com/v1/albums/3D5JoPheRL85pJEg4gZC3G', 'id': '3D5JoPheRL85pJEg4gZC3G', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273b76c039db1579167c4df404f', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02b76c039db1579167c4df404f', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851b76c039db1579167c4df404f', 'width': 64}], 'name': 'The Best of Type O Negative', 'release_date': '2006-09-11', 'release_date_precision': 'day', 'total_tracks': 12, 'type': 'album', 'uri': 'spotify:album:3D5JoPheRL85pJEg4gZC3G'},
    {'album_group': 'compilation', 'album_type': 'compilation', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0blJzvevdXrp21YeI2vbco'}, 'href': 'https://api.spotify.com/v1/artists/0blJzvevdXrp21YeI2vbco', 'id': '0blJzvevdXrp21YeI2vbco', 'name': 'Type O Negative', 'type': 'artist', 'uri': 'spotify:artist:0blJzvevdXrp21YeI2vbco'}], 'available_markets': [], 'external_urls': {'spotify': 'https://open.spotify.com/album/1vvBwbiS6MIDWvinWsKV6i'}, 'href': 'https://api.spotify.com/v1/albums/1vvBwbiS6MIDWvinWsKV6i', 'id': '1vvBwbiS6MIDWvinWsKV6i', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b2733fc946f8cb3465c4f06dcc9c', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e023fc946f8cb3465c4f06dcc9c', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d000048513fc946f8cb3465c4f06dcc9c', 'width': 64}], 'name': 'The Least Worst Of', 'release_date': '2000', 'release_date_precision': 'year', 'total_tracks': 14, 'type': 'album', 'uri': 'spotify:album:1vvBwbiS6MIDWvinWsKV6i'},
    {'album_group': 'appears_on', 'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0LyfQWJT6nXafLPZqxe9Of'}, 'href': 'https://api.spotify.com/v1/artists/0LyfQWJT6nXafLPZqxe9Of', 'id': '0LyfQWJT6nXafLPZqxe9Of', 'name': 'Various Artists', 'type': 'artist', 'uri': 'spotify:artist:0LyfQWJT6nXafLPZqxe9Of'}], 'available_markets': [], 'external_urls': {'spotify': 'https://open.spotify.com/album/1waplfzA8oEtsBdoKzmmuK'}, 'href': 'https://api.spotify.com/v1/albums/1waplfzA8oEtsBdoKzmmuK', 'id': '1waplfzA8oEtsBdoKzmmuK', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b2732c66baf705766e0e7905ee37', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e022c66baf705766e0e7905ee37', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d000048512c66baf705766e0e7905ee37', 'width': 64}], 'name': 'Pure Metal Classics', 'release_date': '2020-07-10', 'release_date_precision': 'day', 'total_tracks': 20, 'type': 'album', 'uri': 'spotify:album:1waplfzA8oEtsBdoKzmmuK'},
    {'album_group': 'appears_on', 'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0LyfQWJT6nXafLPZqxe9Of'}, 'href': 'https://api.spotify.com/v1/artists/0LyfQWJT6nXafLPZqxe9Of', 'id': '0LyfQWJT6nXafLPZqxe9Of', 'name': 'Various Artists', 'type': 'artist', 'uri': 'spotify:artist:0LyfQWJT6nXafLPZqxe9Of'}], 'available_markets': [], 'external_urls': {'spotify': 'https://open.spotify.com/album/4djSahk0SwOlziIPrrfGLO'}, 'href': 'https://api.spotify.com/v1/albums/4djSahk0SwOlziIPrrfGLO', 'id': '4djSahk0SwOlziIPrrfGLO', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273496ef0f2c682daaf7a23d987', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02496ef0f2c682daaf7a23d987', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851496ef0f2c682daaf7a23d987', 'width': 64}], 'name': 'Epic Metal', 'release_date': '2020-07-10', 'release_date_precision': 'day', 'total_tracks': 39, 'type': 'album', 'uri': 'spotify:album:4djSahk0SwOlziIPrrfGLO'},
    {'album_group': 'appears_on', 'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0LyfQWJT6nXafLPZqxe9Of'}, 'href': 'https://api.spotify.com/v1/artists/0LyfQWJT6nXafLPZqxe9Of', 'id': '0LyfQWJT6nXafLPZqxe9Of', 'name': 'Various Artists', 'type': 'artist', 'uri': 'spotify:artist:0LyfQWJT6nXafLPZqxe9Of'}], 'available_markets': [], 'external_urls': {'spotify': 'https://open.spotify.com/album/3VXM5n28tizguvDd5rve5S'}, 'href': 'https://api.spotify.com/v1/albums/3VXM5n28tizguvDd5rve5S', 'id': '3VXM5n28tizguvDd5rve5S', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273c81f0a6236fbf4ba6c4e9bc5', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02c81f0a6236fbf4ba6c4e9bc5', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851c81f0a6236fbf4ba6c4e9bc5', 'width': 64}], 'name': 'Metal for the Masses', 'release_date': '2020-07-10', 'release_date_precision': 'day', 'total_tracks': 47, 'type': 'album', 'uri': 'spotify:album:3VXM5n28tizguvDd5rve5S'},
    {'album_group': 'appears_on', 'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0LyfQWJT6nXafLPZqxe9Of'}, 'href': 'https://api.spotify.com/v1/artists/0LyfQWJT6nXafLPZqxe9Of', 'id': '0LyfQWJT6nXafLPZqxe9Of', 'name': 'Various Artists', 'type': 'artist', 'uri': 'spotify:artist:0LyfQWJT6nXafLPZqxe9Of'}], 'available_markets': [], 'external_urls': {'spotify': 'https://open.spotify.com/album/0zVFgvW9mblEk10KMQxAEC'}, 'href': 'https://api.spotify.com/v1/albums/0zVFgvW9mblEk10KMQxAEC', 'id': '0zVFgvW9mblEk10KMQxAEC', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b2733c7e2cee001941b230d73038', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e023c7e2cee001941b230d73038', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d000048513c7e2cee001941b230d73038', 'width': 64}], 'name': 'Metal Gótico', 'release_date': '2020-07-10', 'release_date_precision': 'day', 'total_tracks': 30, 'type': 'album', 'uri': 'spotify:album:0zVFgvW9mblEk10KMQxAEC'},
    {'album_group': 'appears_on', 'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0LyfQWJT6nXafLPZqxe9Of'}, 'href': 'https://api.spotify.com/v1/artists/0LyfQWJT6nXafLPZqxe9Of', 'id': '0LyfQWJT6nXafLPZqxe9Of', 'name': 'Various Artists', 'type': 'artist', 'uri': 'spotify:artist:0LyfQWJT6nXafLPZqxe9Of'}], 'available_markets': [], 'external_urls': {'spotify': 'https://open.spotify.com/album/0Ie8vTNezXmWiIP8Lutqij'}, 'href': 'https://api.spotify.com/v1/albums/0Ie8vTNezXmWiIP8Lutqij', 'id': '0Ie8vTNezXmWiIP8Lutqij', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273524452f9232c06b79bdc4638', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02524452f9232c06b79bdc4638', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851524452f9232c06b79bdc4638', 'width': 64}], 'name': 'Metall für die Massen', 'release_date': '2020-07-10', 'release_date_precision': 'day', 'total_tracks': 48, 'type': 'album', 'uri': 'spotify:album:0Ie8vTNezXmWiIP8Lutqij'},
    {'album_group': 'appears_on', 'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0LyfQWJT6nXafLPZqxe9Of'}, 'href': 'https://api.spotify.com/v1/artists/0LyfQWJT6nXafLPZqxe9Of', 'id': '0LyfQWJT6nXafLPZqxe9Of', 'name': 'Various Artists', 'type': 'artist', 'uri': 'spotify:artist:0LyfQWJT6nXafLPZqxe9Of'}], 'available_markets': [], 'external_urls': {'spotify': 'https://open.spotify.com/album/67HB1UM44WpMdXlcyDSptr'}, 'href': 'https://api.spotify.com/v1/albums/67HB1UM44WpMdXlcyDSptr', 'id': '67HB1UM44WpMdXlcyDSptr', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273b0a641b5ad90718a11821a78', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02b0a641b5ad90718a11821a78', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851b0a641b5ad90718a11821a78', 'width': 64}], 'name': 'Metal Destroyers', 'release_date': '2020-07-03', 'release_date_precision': 'day', 'total_tracks': 29, 'type': 'album', 'uri': 'spotify:album:67HB1UM44WpMdXlcyDSptr'},
    {'album_group': 'appears_on', 'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0LyfQWJT6nXafLPZqxe9Of'}, 'href': 'https://api.spotify.com/v1/artists/0LyfQWJT6nXafLPZqxe9Of', 'id': '0LyfQWJT6nXafLPZqxe9Of', 'name': 'Various Artists', 'type': 'artist', 'uri': 'spotify:artist:0LyfQWJT6nXafLPZqxe9Of'}], 'available_markets': [], 'external_urls': {'spotify': 'https://open.spotify.com/album/4m5tC75P6X3vxQQWdTeWGF'}, 'href': 'https://api.spotify.com/v1/albums/4m5tC75P6X3vxQQWdTeWGF', 'id': '4m5tC75P6X3vxQQWdTeWGF', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b27353a465520ab796b0d1a5d176', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e0253a465520ab796b0d1a5d176', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d0000485153a465520ab796b0d1a5d176', 'width': 64}], 'name': 'Party Metal', 'release_date': '2020-06-19', 'release_date_precision': 'day', 'total_tracks': 25, 'type': 'album', 'uri': 'spotify:album:4m5tC75P6X3vxQQWdTeWGF'},
    {'album_group': 'appears_on', 'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0LyfQWJT6nXafLPZqxe9Of'}, 'href': 'https://api.spotify.com/v1/artists/0LyfQWJT6nXafLPZqxe9Of', 'id': '0LyfQWJT6nXafLPZqxe9Of', 'name': 'Various Artists', 'type': 'artist', 'uri': 'spotify:artist:0LyfQWJT6nXafLPZqxe9Of'}], 'available_markets': [], 'external_urls': {'spotify': 'https://open.spotify.com/album/2c07WUUstLP86KyrZ7ExRR'}, 'href': 'https://api.spotify.com/v1/albums/2c07WUUstLP86KyrZ7ExRR', 'id': '2c07WUUstLP86KyrZ7ExRR', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273f3f433fc021f67bf96995cfd', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02f3f433fc021f67bf96995cfd', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851f3f433fc021f67bf96995cfd', 'width': 64}], 'name': 'Children of Goth', 'release_date': '2020-06-19', 'release_date_precision': 'day', 'total_tracks': 25, 'type': 'album', 'uri': 'spotify:album:2c07WUUstLP86KyrZ7ExRR'}
    ]
"""