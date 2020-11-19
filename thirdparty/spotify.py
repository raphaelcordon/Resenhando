import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = '458d767d30034a44828d668093119d4f'
CLIENT_SECRET = '94362b7769f64dd298ae57852647527b'

SPOTIFY = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET))


#  <-- Artist Spotify searches -->
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
        for item in SPOTIFY.search(q='artist:' + self.name, type='artist')['artists']['items'][:5]:
            image = item['images'][0]['url'] if len(item['images']) > 0 else ''
            if image != '':
                radio = str.replace(
                    item['external_urls']['spotify'], "/artist/", "/embed/artist/")
                artist = {'id':     item['id'],
                          'name':   item['name'],
                          'image':  image,
                          'uri':    item['uri'],
                          'genres': item['genres'],
                          'radio':  radio
                          }
                self.listArtists.append(artist)
        return self.listArtists


class SpotifyGetOneArtist:
    def __init__(self, artistID):
        """
        Returns an artist accordingly the id
        The id is selected from one of the 5 artists
        from the class: SpotifyGetFiveArtists
        :param artistID: id from selected artist
        """
        self.artistID = artistID
        self.oneArtist = []
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
                          'radio':  radio,
                          'spotifyId': artistSearch['id']
                          }
        return self.oneArtist


#  <-- Album Spotify searches -->
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

                # Get album id to get the genre (only artists have genres)
                albumSearch = SPOTIFY.album(self.item['id'])
                genres = SPOTIFY.artist(albumSearch['artists'][0]['id'])['genres']

                album = {'id': self.item['id'],
                         'name': self.item['name'],
                         'image': image,
                         'artist_name': artist_name,
                         'release_date': self.item['release_date'][:4],
                         'genres': genres,
                         'radio': radio,
                         'totalTracks': self.item['total_tracks']
                         }

                if not self.__contains(album_name):
                    self.listAlbums.append(album)

        return self.listAlbums

    def __contains(self, album_name):
        exclusionList = ["- ", " (Deluxe Edition)", " (Deluxe Version)", " (Expanded Edition)", " (Deluxe)",
                         " (Remastered)", " (Bonus Track Edition)", " (2007 Remaster)", " (2008 Remaster)",
                         " (2009 Remaster)", " (2010 Remaster)", " (2011 Remaster)", " (2012 Remaster)",
                         " (2013 Remaster)", " (2014 Remaster)", " (2015 Remaster)", " (2016 Remaster)",
                         " (2017 Remaster)", " (2018 Remaster)", " (2019 Remaster)", " (2020 Remaster)",
                         " (1994 Remaster)", " (Remastered Deluxe Box Set)", " (Super Deluxe Edition)",
                         " (Deluxe Remaster)", " (Deluxe / Remastered)", " (Collector's Edition)",
                         " (Deluxe Box Set / Remastered)", " (2011 Remastered Version)", " (Expanded)",
                         " [Remastered] (Remastered Version)", " [2011 - Remaster] (2011 Remastered Version)",
                         " (Expanded Bonus Track Edition)", " [Expanded & Remastered]", " (10th Anniversary Edition)",
                         " (10th Anniversary Edition) [Deluxe]", " (ARIA Awards Edition)", " (Japan Version)",
                         " (International Explicit Nokia Exclusive Version)", " (Japan Version)", " (Edited)",
                         " (Explicit)", " (Deluxe Edited)", " (Deluxe Version [Edited])", " (Standard Version [Edited])",
                         ]
        for item in self.listAlbums:
            for i in exclusionList:
                itemList = str.replace(item['name'], i, "")
                compareAlbumName = str.replace(album_name, i, "")

                if itemList.lower() == compareAlbumName.lower() \
                        or compareAlbumName in self.listAlbums:
                    return True


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
                         'artistId': albumSearch['artists'][0]['id'],
                         'artistName': albumSearch['artists'][0]['name']
                         }
        return self.oneAlbum


#  <-- Playlist Spotify searches -->
class SpotifyGetPlaylists:
    def __init__(self, spotifyUser):
        """
        Returns playlists accordingly to Spotify's username
        :param spotifyUser: from user's typing
        """
        self.spotifyUser = spotifyUser
        self.playlists = []
        self.createList()

    def createList(self):
        if not SPOTIFY.user(self.spotifyUser):
            return False
        else:
            for item in SPOTIFY.user_playlists(self.spotifyUser)['items']:
                image = item['images'][0]['url'] if len(item['images']) > 0 else ''
                radio = str.replace(
                    item['external_urls']['spotify'], "/playlist/", "/embed/playlist/")
                playlist = {
                    'id': item['id'],
                    'name': item['name'],
                    'image': image,
                    'radio': radio
                }
                if playlist not in self.playlists:
                    self.playlists.append(playlist)
            return self.playlists


class SpotifyGetOnePlaylist:
    def __init__(self, playlistID):
        """
        Returns a playlist accordingly the id
        FUNCTION TO BE CREATED IN THE WEBSITE
        :param playlistID: id from selected playlist
        """
        self.playlistID = playlistID
        self.onePlaylist = {}
        self.createList()

    def createList(self):
        artistSearch = SPOTIFY.playlist(self.playlistID)
        image = artistSearch['images'][0]['url'] if len(
            artistSearch['images']) > 0 else ''
        radio = str.replace(
            artistSearch['external_urls']['spotify'], "/playlist/", "/embed/playlist/")
        self.onePlaylist = {'id':     artistSearch['id'],
                            'name':   artistSearch['name'],
                            'image':  image,
                            'uri':    artistSearch['uri'],
                            'tracks': artistSearch['tracks']['total'],
                            'radio':  radio
                            }
        return self.onePlaylist


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


#  <-- Track Spotify searches -->
class SpotifyGetOneTrack:
    def __init__(self, trackId):
        """
        Returns a Track accordingly the id
        The id is selected from one album
        FUNCTIO TO BE CREATED IN THE WEBSITE
        :param trackId: id from selected Track
        """
        self.trackId = trackId
        self.oneTrack = {}
        self.createList()

    def createList(self):
        track = SPOTIFY.track(self.trackId)
        image = track['album']['images'][0]['url'] if len(
            track['album']['images']) > 0 else ''
        radio = str.replace(
            track['external_urls']['spotify'], "/track/", "/embed/track/")
        genres = SPOTIFY.artist(track['artists'][0]['id'])['genres']
        self.oneTrack = {'id':     track['id'],
                         'name':   track['name'],
                         'image':  image,
                         'radio':  radio,
                         'releaseDate': track['album']['release_date'][:4],
                         'genres': genres,
                         'artistId': track['artists'][0]['id'],
                         'artistName': track['artists'][0]['name'],
                         'albumName': track['album']['name']
                         }

        return self.oneTrack


class SpotifyGetTracks:
    def __init__(self, spotifyTracks):
        """
        Returns tracks accordingly to the search
        :param spotifyTracks: from user's typing
        """
        self.spotifyTracks = spotifyTracks
        self.track = {}
        self.tracks = []
        self.createList()

    def createList(self):
        for item in SPOTIFY.search(self.spotifyTracks, type='track')['tracks']['items']:
            image = item['album']['images'][0]['url'] if len(
                item['album']['images']) > 0 else ''
            radio = str.replace(
                item['external_urls']['spotify'], "/track/", "/embed/track/")
            self.track = {'id':     item['id'],
                          'name':   item['name'],
                          'image':  image,
                          'radio':  radio,
                          'artistName': item['artists'][0]['name']
                          }
            self.tracks.append(self.track)
        return self.tracks
