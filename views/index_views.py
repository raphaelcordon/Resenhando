from flask import render_template, session, redirect, url_for, Blueprint
from thirdparty.spotify import SpotifyGetOneAlbum, SpotifyGetOneArtist
from repository.users_repos import UsersRepository
from repository.resenha_repos import ResenhaRepository
from models.index_model import IndexSpotify

ind = Blueprint('ind', __name__, url_prefix='')


@ind.route('/')
def index():
    __createSessionVariables()
    return redirect(url_for('ind.home'))


@ind.route('/home/')
def home():
    spotifyArtist = []
    spotifyAlbum = []
    spotifyTrack = []
    spotifyPlaylist = []

    reviews = ResenhaRepository().List()
    for item in reviews:
        if item.tipo_review == 'artista':
            spotifyArtist.append(SpotifyGetOneArtist(item.spotify_id).oneArtist)
        elif item.tipo_review == 'album':
            spotifyAlbum.append(SpotifyGetOneAlbum(item.spotify_id).oneAlbum)

    print(spotifyArtist)
    users = UsersRepository().List()
    return render_template('index.html', reviews=reviews, users=users, spotifyArtist=spotifyArtist,
                           spotifyAlbum=spotifyAlbum, spotifyTrack=spotifyTrack, spotifyPlaylist=spotifyPlaylist)


@ind.route('/home/<ordering>/')
def home_ordering(ordering):
    review = ResenhaRepository().List()
    users = UsersRepository().List()

    return render_template('index.html', resenhas=review, users=users, ordering=ordering)


def __createSessionVariables():
    session['id'] = ''
    session['username'] = ''
    session['name'] = ''
    session['surname'] = ''
    session['access_level'] = ''
    session['nome_review'] = ''
    session['nome_banda'] = ''
    session['review'] = ''
