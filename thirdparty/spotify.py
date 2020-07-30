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
                artist = {'id':     item['id'],
                          'name':   item['name'],
                          'image':  image,
                          'uri':    item['uri'],
                          'genres': item['genres']
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
                          'radio':  radio
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

                album = {'id': self.item['id'],
                         'name': self.item['name'],
                         'image': image,
                         'artist_name': artist_name,
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

        album_name7 = album_name
        album_name7 = str.replace(album_name7, " (Bonus Track Edition)", "")
        for item in self.listAlbums:
            name = str.replace(item['name'], " (Bonus Track Edition)", "")
            if album_name7 == name:
                return True

        album_name8 = album_name
        album_name8 = str.replace(album_name8, " (2010 Remaster)", "")
        for item in self.listAlbums:
            name = str.replace(item['name'], " (2010 Remaster)", "")
            if album_name8 == name:
                return True

        album_name9 = album_name
        album_name9 = str.replace(album_name9, " (2011 Remaster)", "")
        for item in self.listAlbums:
            name = str.replace(item['name'], " (2011 Remaster)", "")
            if album_name9 == name:
                return True

        album_name10 = album_name
        album_name10 = str.replace(album_name10, " (2012 Remaster)", "")
        for item in self.listAlbums:
            name = str.replace(item['name'], " (2012 Remaster)", "")
            if album_name10 == name:
                return True

        album_name11 = album_name
        album_name11 = str.replace(album_name11, " (2013 Remaster)", "")
        for item in self.listAlbums:
            name = str.replace(item['name'], " (2013 Remaster)", "")
            if album_name11 == name:
                return True

        album_name12 = album_name
        album_name12 = str.replace(album_name12, " (2014 Remaster)", "")
        for item in self.listAlbums:
            name = str.replace(item['name'], " (2014 Remaster)", "")
            if album_name12 == name:
                return True

        album_name13 = album_name
        album_name13 = str.replace(album_name13, " (2015 Remaster)", "")
        for item in self.listAlbums:
            name = str.replace(item['name'], " (2015 Remaster)", "")
            if album_name13 == name:
                return True

        album_name14 = album_name
        album_name14 = str.replace(album_name14, " (2016 Remaster)", "")
        for item in self.listAlbums:
            name = str.replace(item['name'], " (2016 Remaster)", "")
            if album_name14 == name:
                return True

        album_name15 = album_name
        album_name15 = str.replace(album_name15, " (2017 Remaster)", "")
        for item in self.listAlbums:
            name = str.replace(item['name'], " (2017 Remaster)", "")
            if album_name15 == name:
                return True

        album_name16 = album_name
        album_name16 = str.replace(album_name16, " (2018 Remaster)", "")
        for item in self.listAlbums:
            name = str.replace(item['name'], " (2018 Remaster)", "")
            if album_name16 == name:
                return True

        album_name17 = album_name
        album_name17 = str.replace(album_name17, " (2019 Remaster)", "")
        for item in self.listAlbums:
            name = str.replace(item['name'], " (2019 Remaster)", "")
            if album_name17 == name:
                return True

        album_name18 = album_name
        album_name18 = str.replace(album_name18, " (2020 Remaster)", "")
        for item in self.listAlbums:
            name = str.replace(item['name'], " (2020 Remaster)", "")
            if album_name18 == name:
                return True

        album_name19 = album_name
        album_name19 = str.replace(album_name19, " (1994 Remaster)", "")
        for item in self.listAlbums:
            name = str.replace(item['name'], " (1994 Remaster)", "")
            if album_name19 == name:
                return True

        return False


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
        self.oneAlbum = {'id':     albumSearch['id'],
                         'name':   albumSearch['name'],
                         'image':  image,
                         'releaseDate': albumSearch['release_date'][:4],
                         'genres': albumSearch['genres'],
                         'radio':  radio,
                         'artistName': albumSearch['artists'][0]['name']
                         }
        return self.oneAlbum


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
        artistSearch = SPOTIFY.track(self.trackId)
        image = artistSearch['album']['images'][0]['url'] if len(
            artistSearch['album']['images']) > 0 else ''
        radio = str.replace(
            artistSearch['external_urls']['spotify'], "/track/", "/embed/track/")
        self.oneTrack = {'id':     artistSearch['id'],
                         'name':   artistSearch['name'],
                         'image':  image,
                         'uri':    artistSearch['uri'],
                         'radio':  radio
                         }
        return self.oneTrack


#  <-- Playlist Spotify searches -->
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
        if not SPOTIFY.user(self.spotifyUser):
            return False
        else:
            for item in SPOTIFY.user_playlists(self.spotifyUser)['items']:
                image = item['images'][0]['url'] if len(
                    item['images']) > 0 else ''
                radio = str.replace(
                    item['external_urls']['spotify'], "/playlist/", "/embed/playlist/")
                self.playlist = {'id':     item['id'],
                              'name':   item['name'],
                              'image':  image,
                              'tracks': item['tracks']['total'],
                              'radio':  radio
                              }
                self.playlists.append(self.playlist)
            return self.playlists


class SpotifyGetOnePlaylist:
    def __init__(self, playlistID):
        """
        Returns a playlist accordingly the id
        FUNCTIO TO BE CREATED IN THE WEBSITE
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
