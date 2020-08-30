from flask import render_template, session, redirect, url_for, Blueprint
from thirdparty.spotify import SpotifyGetOneAlbum, SpotifyGetOneArtist, SpotifyGetOneTrack, SpotifyGetOnePlaylist
from repository.users_repos import UsersRepository
from repository.resenha_repos import ResenhaRepository
from passlib.hash import sha1_crypt

ind = Blueprint('ind', __name__, url_prefix='')


@ind.route('/')
def index():
    if 'id' not in session:
        __createSessionVariables()
    spotifyArtist = []
    spotifyAlbum = []
    spotifyTrack = []
    spotifyPlaylist = []

    users = UsersRepository().List()
    reviewsArtist = ResenhaRepository().List('artista', 6)
    reviewsAlbum = ResenhaRepository().List('album', 6)
    reviewsTrack = ResenhaRepository().List('track', 6)
    reviewsPlaylist = ResenhaRepository().List('playlist', 6)
    for item in reviewsArtist:
        spotifyArtist.append(SpotifyGetOneArtist(item.spotify_id).oneArtist)
    for item in reviewsAlbum:
        spotifyAlbum.append(SpotifyGetOneAlbum(item.spotify_id).oneAlbum)
    for item in reviewsTrack:
        spotifyTrack.append(SpotifyGetOneTrack(item.spotify_id).oneTrack)
    for item in reviewsPlaylist:
        spotifyPlaylist.append(
            SpotifyGetOnePlaylist(item.spotify_id).onePlaylist)

    return render_template('index.html', reviewsArtist=reviewsArtist, reviewsAlbum=reviewsAlbum,
                           reviewsTrack=reviewsTrack, reviewsPlaylist=reviewsPlaylist,
                           users=users, spotifyArtist=spotifyArtist, spotifyAlbum=spotifyAlbum,
                           spotifyTrack=spotifyTrack, spotifyPlaylist=spotifyPlaylist, mainFilter='index')


@ind.route('/home/')
def home():

    return redirect(url_for('ind.index'))


def __createSessionVariables():
    session['id'] = ''
    session['name'] = ''
    session['surname'] = ''
    session['email'] = ''
    session['access_level'] = ''
    session['nome_review'] = ''
    session['nome_banda'] = ''
    session['review'] = ''
    session['previous'] = ''
