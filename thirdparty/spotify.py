import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re

CLIENT_ID = '458d767d30034a44828d668093119d4f'
CLIENT_SECRET = '94362b7769f64dd298ae57852647527b'


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