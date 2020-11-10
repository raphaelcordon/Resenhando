import spotipy
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
                image = self.item['images'][0]['url'] if len(
                    self.item['images']) > 0 else ''
                artist_name = self.item['artists'][0]['name'] if len(
                    self.item['artists']) > 0 else ''
                album_name = self.item['name']
                radio = str.replace(
                    self.item['external_urls']['spotify'], "/album/", "/embed/album/")
                albumSearch = SPOTIFY.album(self.item['id'])
                genres = SPOTIFY.artist(albumSearch['artists'][0]['id'])['genres']

                album = {'id': self.item['id'],
                         'name': self.item['name'],
                         'image': image,
                         'artist_name': artist_name,
                         'release_date': self.item['release_date'][:4],
                         'radio': radio,
                         'totalTracks': self.item['total_tracks'],
                         'genres': genres
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

#get = SpotifyGetAlbums('4lgrzShsg2FLA89UM2fdO5')
#print(get.albums)
#for g in get.listAlbums:
#    print(g)


'''
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


get = SpotifyGetFiveArtists('Iron Maiden')
for g in get.listArtists:
    print(g)
'''


class SpotifyGetOneArtist:
    def __init__(self, artistID):
        """
        Returns an artist accordingly the id
        The id is selected from one of the 5 artists
        from the class: SpotifyGetFiveArtists
        :param artistID: id from selected artist
        """
        self.artistID = artistID
        self.oneArtist = {}
        self.oneArtistTopTrack = []
        self.createList()

    def createList(self):
        artistSearch = SPOTIFY.artist(self.artistID)
        image = artistSearch['images'][0]['url'] if len(
            artistSearch['images']) > 0 else ''
        radio = str.replace(
            artistSearch['external_urls']['spotify'], "/artist/", "/embed/artist/")
        self.oneArtist = {'id':     artistSearch['id'],
                          'name':   artistSearch['name'],
                          'image':  image,
                          'uri':    artistSearch['uri'],
                          'genres': artistSearch['genres'],
                          'radio':  radio
                          }
        return self.oneArtist

artist = SPOTIFY.artist("2nRyqv8aTwpdazeAg0lOQK")
print(artist)

class SpotifyGetOneAlbum:
    def __init__(self, albumID):
        """
        Returns an album accordingly the id
        The id is selected from album list
        from the class: SpotifyGetAlbums
        :param albumID: id from selected album
        """
        self.albumID = albumID
        self.oneAlbum = {}
        self.createList()

    def createList(self):
        albumSearch = SPOTIFY.album(self.albumID)
        image = albumSearch['images'][0]['url'] if len(
            albumSearch['images']) > 0 else ''
        radio = str.replace(
            albumSearch['external_urls']['spotify'], "/album/", "/embed/album/")
        genres = SPOTIFY.artist(albumSearch['artists'][0]['id'])['genres']
        self.oneAlbum = {'id':     albumSearch['id'],
                         'name':   albumSearch['name'],
                         'image':  image,
                         'releaseDate': albumSearch['release_date'][:4],
                         'genres': genres,
                         'radio':  radio,
                         'artistName': albumSearch['artists'][0]['name']
                         }
        return self.oneAlbum

#print(SpotifyGetOneAlbum('7JPsPwLr67TEfChdr86yIU').createList())

"""

{'album_type': 'album', 
'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6mdiAmATAx73kdxrNrnlao'}, 'href': 'https://api.spotify.com/v1/artists/6mdiAmATAx73kdxrNrnlao', 'id': '6mdiAmATAx73kdxrNrnlao', 'name': 'Iron Maiden', 'type': 'artist', 'uri': 'spotify:artist:6mdiAmATAx73kdxrNrnlao'}], 
'external_urls': {'spotify': 'https://open.spotify.com/album/6iVSpex7UohpwPOYZEYmvm'}, 
'href': 'https://api.spotify.com/v1/albums/6iVSpex7UohpwPOYZEYmvm', 'id': '6iVSpex7UohpwPOYZEYmvm', 
'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273291b0e8f1a74c2bc9f9d3110', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02291b0e8f1a74c2bc9f9d3110', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851291b0e8f1a74c2bc9f9d3110', 'width': 64}], 
'name': 'Piece of Mind (2015 - Remaster)', 
'release_date': '1983-05-16', 
'release_date_precision': 'day', 
'total_tracks': 9, 
'type': 'album', 
'uri': 'spotify:album:6iVSpex7UohpwPOYZEYmvm'}, 
'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6mdiAmATAx73kdxrNrnlao'}, 'href': 'https://api.spotify.com/v1/artists/6mdiAmATAx73kdxrNrnlao', 'id': '6mdiAmATAx73kdxrNrnlao', 'name': 'Iron Maiden', 'type': 'artist', 'uri': 'spotify:artist:6mdiAmATAx73kdxrNrnlao'}], 
'disc_number': 1, 
'duration_ms': 252733, 
'explicit': False, 
'external_ids': {'isrc': 'GBCHB1800032'}, 
'external_urls': {'spotify': 'https://open.spotify.com/track/1Ab3hhOw1TJWDgO10vlxNZ'}, 
'href': 'https://api.spotify.com/v1/tracks/1Ab3hhOw1TJWDgO10vlxNZ', 
'id': '1Ab3hhOw1TJWDgO10vlxNZ', 
'is_local': False, 
'is_playable': True, 
'name': 'The Trooper - 2015 Remaster',
 'popularity': 60, 
'preview_url': 'https://p.scdn.co/mp3-preview/0a88f3e6d8e5dfe20807b9a4ee1cf1f30fa871d2?cid=458d767d30034a44828d668093119d4f', 
'track_number': 5, 
'type': 'track', 
'uri': 'spotify:track:1Ab3hhOw1TJWDgO10vlxNZ'
    }
"""


class SpotifyGetOnePlaylist:
    def __init__(self, playlistID):
        """
        Returns an artist accordingly the id
        The id is selected from one of the 5 artists
        from the class: SpotifyGetFiveArtists
        :param artistID: id from selected artist
        """
        self.playlistID = playlistID
        self.onePlaylist = {}
        self.createList()

    def createList(self):
        print(SPOTIFY.playlist(self.playlistID))
        artistSearch = SPOTIFY.playlist(self.playlistID)
        image = artistSearch['images'][0]['url'] if len(
            artistSearch['images']) > 0 else ''
        radio = str.replace(
            artistSearch['external_urls']['spotify'], "/playlist/", "/embed/playlist/")
        self.playlist = {'id':     artistSearch['id'],
                         'name':   artistSearch['name'],
                         'image':  image,
                         'uri':    artistSearch['uri'],
                         'radio':  radio
                         }
        return self.playlist

"""
class SpotifyGetOneTrack:
    def __init__(self, trackId):

        self.trackId = trackId
        self.oneTrack = {}
        self.createList()

    def createList(self):
        artistSearch = SPOTIFY.track(self.trackId)
        image = artistSearch['album']['images'][0]['url'] if len(
            artistSearch['album']['images']) > 0 else ''
        radio = str.replace(
            artistSearch['external_urls']['spotify'], "/track/", "/embed/track/")
        self.track = {'id':     artistSearch['id'],
                      'name':   artistSearch['name'],
                      'image':  image,
                      'uri':    artistSearch['uri'],
                      'radio':  radio
                      }
        return self.track


get = SpotifyGetOneTrack('3tqv7xESjYRUjnBoJvfLhN').createList()
print(get)

"""

class SpotifyGetPlaylists:
    def __init__(self, spotifyUser):
        """
        Returns playlists accordingly to Spotify's username
        :param spotifyUser: from user's typing
        """
        self.spotifyUser = spotifyUser
        self.playlist = {}
        self.playlists = []
        self.createList()

    def createList(self):
        for item in SPOTIFY.user_playlists(self.spotifyUser)['items']:
            image = item['images'][0]['url'] if len(item['images']) > 0 else ''
            radio = str.replace(item['external_urls']['spotify'], "/playlist/", "/embed/playlist/")
            playlist = {
                'id':     item['id'],
                'name':   item['name'],
                'image':  image,
                'radio':  radio
            }
            if playlist not in self.playlists:
                self.playlists.append(playlist)
        return self.playlists


#for f in SpotifyGetPlaylists('raphaelcordon').createList():
#    print(f)

#for f in SPOTIFY.user_playlists('raphaelcordon')['items']:
#    print(f)


"""
{'href': 'https://api.spotify.com/v1/users/raphaelcordon/playlists?offset=0&limit=50', 
 'items': [
     {'collaborative': False, 
      'description': '', 
      'external_urls': {'spotify': 'https://open.spotify.com/playlist/6KEiQ9Ehr325Ue66PsMxDX'}, 
      'href': 'https://api.spotify.com/v1/playlists/6KEiQ9Ehr325Ue66PsMxDX', 
      'id': '6KEiQ9Ehr325Ue66PsMxDX', 
      'images': [{'height': 640, 'url': 'https://mosaic.scdn.co/640/ab67616d0000b27324f01aae2352e0a1122af658ab67616d0000b2733da79014d89a8e58650c8292ab67616d0000b2739ce3670bb54ff6b1a0452dafab67616d0000b273e94f9420e4b721f2c9a78377', 'width': 640} 
      'name': 'Bruce', 
      'owner': {'display_name': 'raphaelcordon', 'external_urls': {'spotify': 'https://open.spotify.com/user/raphaelcordon'}, 'href': 'https://api.spotify.com/v1/users/raphaelcordon', 'id': 'raphaelcordon', 'type': 'user', 'uri': 'spotify:user:raphaelcordon'}, 
      'primary_color': None, 
      'public': True, 
      'snapshot_id': 'MTksZTc4OTgyOTk3ZjAxNTE0NTE4OTQ0NWVkZjlkNzMzNDJiNWRhOTVmOA==', 
      'tracks': {'href': 'https://api.spotify.com/v1/playlists/6KEiQ9Ehr325Ue66PsMxDX/tracks', 'total': 17}, 
      'type': 'playlist', 
      'uri': 'spotify:playlist:6KEiQ9Ehr325Ue66PsMxDX'
      }], 
     'limit': 50, 'next': None, 'offset': 0, 'previous': None, 'total': 2}

"""


class SpotifyCheckUser:
    def __init__(self, spotifyUser):
        """
        Returns True/False accordingly to Spotify's username
        :param spotifyUser: from user's typing
        """
        self.spotifyUser = spotifyUser
    def checkUser(self):
        try:
            if SPOTIFY.user(self.spotifyUser):
                return True
        except:
            pass


class SpotifyGetTracks:
    def __init__(self, spotifyTracks):
        """
        Returns playlists accordingly to Spotify's username
        :param spotifyUser: from user's typing
        """
        self.spotifyTracks = spotifyTracks
        self.track = {}
        self.tracks = []
        self.createList()

    def createList(self):
        print(SPOTIFY.search('Breakthru', type='track')['tracks']['items'])
        for item in SPOTIFY.search(self.spotifyTracks, type='track')['tracks']['items']:
            image = item['album']['images'][0]['url'] if len(
                item['album']['images']) > 0 else ''
            radio = str.replace(
                item['external_urls']['spotify'], "/track/", "/embed/track/")
            self.track = {'id':     item['id'],
                          'name':   item['name'],
                          'image':  image,
                          'radio':  radio,
                          'releaseDate': item['album']['release_date'][:4],
                          'artistName': item['artists'][0]['name'],
                          'albumName': item['album']['name']

                             }
            self.tracks.append(self.track)
        return self.tracks


#for f in SpotifyGetTracks('Breakthru').createList():
#    print(f)


# -----------------
