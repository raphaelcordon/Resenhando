from flask import url_for, render_template, request, redirect, Blueprint
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re


CLIENT_ID = '458d767d30034a44828d668093119d4f'
CLIENT_SECRET = '94362b7769f64dd298ae57852647527b'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

tes = Blueprint('tes', __name__)


@tes.route('/spotify')
def testeSpotify():
    return render_template('teste.html')


@tes.route('/pesquisa', methods=['GET', 'POST'])
def pesquisa():
    artists = getFiveArtists(request.form['artista']).listArtists

    return render_template('testeresposta.html', artists=artists)


class getFiveArtists:
    def __init__(self, name):
        self.name = name
        self.listArtists = []
        self.createList()

    def createList(self):
        for list in spotify.search(q='artist:' + self.name, type='artist')['artists']['items'][:5]:
            artist = {'id':     list['id'],
                      'name':   list['name'],
                      'image': list['images'][0]['url'],
                      'uri':    list['uri'],
                      'genres': list['genres']
                      }
            self.listArtists.append(artist)
        return self.listArtists
