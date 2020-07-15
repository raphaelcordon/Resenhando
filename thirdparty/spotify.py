import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re

CLIENT_ID = '458d767d30034a44828d668093119d4f'
CLIENT_SECRET = '94362b7769f64dd298ae57852647527b'

SPOTIFY = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

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

class SpotifyLink:
    def __init__(self, address: str):
        """
        Returns:
            Hyperlink for Spotify radio
        :parameter
            address (str): Gets the address from the 'resenha' or 'editar_resenha' in templates
        :returns
            self.spotify (str): The string to be read at 'resenhando' in templates
        """
        self.address = str(address)
        self.segment = ''
        self.link = ''
        self.image_link = ''

        if 'album:' in self.address:
            self.segment = 'album'
            self.link = re.search(r'(?<=album:)\w+', self.address).group(0)
        elif 'album/' in self.address:
            self.segment = 'album'
            self.link = re.search(r'(?<=album/)\w+', self.address).group(0)
        elif 'track:' in self.address:
            self.segment = 'track'
            self.link = re.search(r'(?<=track:)\w+', self.address).group(0)
        elif 'track/' in self.address:
            self.segment = 'track'
            self.link = re.search(r'(?<=track/)\w+', self.address).group(0)
        elif 'playlist:' in self.address:
            self.segment = 'playlist'
            self.link = re.search(r'(?<=playlist:)\w+', self.address).group(0)
        elif 'playlist/' in self.address:
            self.segment = 'playlist'
            self.link = re.search(r'(?<=playlist/)\w+', self.address).group(0)

    def __str__(self):
        if self.segment == '' or self.link == '':
            return ''
        else:
            return str(f'https://open.spotify.com/embed/{self.segment}/{self.link}')


class SpotifyImage:
    def __init__(self, address: str):
        """
        Returns:
            The image from the hyperlink
        :parameter
            address (str): Gets the address from the 'resenha' or 'editar_resenha' in templates
        :returns
            self.image_link (str): the string to be read at 'resenhando' in templates
        """
        self.address = str(address)
        self.image_link = ''

        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
            client_id=CLIENT_ID, client_secret=CLIENT_SECRET))
        if 'album' in self.address:
            self.image_link = str(spotify.album(
                self.address)['images'][0]['url'])
        elif 'track' in self.address:
            self.image_link = str(spotify.track(self.address)[
                                  'album']['images'][0]['url'])
        elif 'playlist' in self.address:
            self.image_link = str(
                spotify.playlist_cover_image(self.address)[0]['url'])

    def __str__(self):
        return self.image_link


class SpotifyTipoResenha:
    def __init__(self, address: str):
        """
        Returns:
            The image from the hyperlink
        :parameter
            address (str): Gets the address from the 'resenha' or 'editar_resenha' in templates
        :returns
            self.tipo_resenha (str): the string to be read at 'resenhando' in templates
        """
        self.address = str(address)
        self.tipo_resenha = ''

        # spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
        #    client_id=CLIENT_ID, client_secret=CLIENT_SECRET))
        if 'album' in self.address:
            self.tipo_resenha = 'album'
        elif 'track' in self.address:
            self.tipo_resenha = 'track'
        elif 'playlist' in self.address:
            self.tipo_resenha = 'playlist'

    def __str__(self):
        return self.tipo_resenha
