from flask import render_template, session, redirect, url_for, Blueprint, flash
from thirdparty.spotify import SpotifyGetOneAlbum, SpotifyGetOneArtist, SpotifyGetOneTrack, SpotifyGetOnePlaylist
from repository.users_repos import UsersRepository
from repository.resenha_repos import ResenhaRepository

filter = Blueprint('filter', __name__, url_prefix='')


@filter.route('/everything')
def everything():

    if 'id' not in session:
        session['id'] = ''

    spotifyArtist = []
    spotifyAlbum = []
    spotifyTrack = []
    spotifyPlaylist = []

    users = UsersRepository().List()
    reviewsArtist = ResenhaRepository().List('artista')
    reviewsAlbum = ResenhaRepository().List('album')
    reviewsTrack = ResenhaRepository().List('track')
    reviewsPlaylist = ResenhaRepository().List('playlist')
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


@filter.route('/filterArtist')
def filterArtist():

    if 'id' not in session:
        session['id'] = ''

    spotifyArtist = []

    users = UsersRepository().List()
    reviewsArtist = ResenhaRepository().List('artista')

    for item in reviewsArtist:
        spotifyArtist.append(SpotifyGetOneArtist(item.spotify_id).oneArtist)

    return render_template('index.html', reviewsArtist=reviewsArtist, spotifyArtist=spotifyArtist,
                           users=users, mainFilter='artist')


@filter.route('/filterAlbum')
def filterAlbum():

    if 'id' not in session:
        session['id'] = ''

    spotifyAlbum = []


    users = UsersRepository().List()
    reviewsAlbum = ResenhaRepository().List('album')
    for item in reviewsAlbum:
        spotifyAlbum.append(SpotifyGetOneAlbum(item.spotify_id).oneAlbum)

    return render_template('index.html', reviewsAlbum=reviewsAlbum, spotifyAlbum=spotifyAlbum,
                           users=users, mainFilter='album')


@filter.route('/filterTrack')
def filterTrack():

    if 'id' not in session:
        session['id'] = ''

    spotifyTrack = []

    users = UsersRepository().List()
    reviewsTrack = ResenhaRepository().List('track')
    for item in reviewsTrack:
        spotifyTrack.append(SpotifyGetOneTrack(item.spotify_id).oneTrack)

    return render_template('index.html', reviewsTrack=reviewsTrack, spotifyTrack=spotifyTrack,
                           users=users, mainFilter='track')


@filter.route('/filterPlaylist')
def filterPlaylist():

    if 'id' not in session:
        session['id'] = ''

    spotifyPlaylist = []

    users = UsersRepository().List()
    reviewsPlaylist = ResenhaRepository().List('playlist')
    for item in reviewsPlaylist:
        spotifyPlaylist.append(
            SpotifyGetOnePlaylist(item.spotify_id).onePlaylist)

    return render_template('index.html', reviewsPlaylist=reviewsPlaylist, spotifyPlaylist=spotifyPlaylist,
                           users=users, mainFilter='playlist')


@filter.route('/home/<int:id>/')
def minhas_resenhas(id):
    if session['email'] == '' or 'email' not in session or session['id'] == '':
        flash('Você precisa logar para acessar essa área', 'info')
        return redirect(url_for('log.login'))

    if 'id' not in session:
        session['id'] = ''

    reviews = ResenhaRepository().FindAuthorById(id)
    if not reviews:

        flash('Você ainda não criou nenhuma resenha', 'info')
        return redirect(url_for('ind.home'))
    else:
        flash('Essas são as resenhas criadas por você até o momento', 'info')

        spotifyArtist = []
        spotifyAlbum = []
        spotifyTrack = []
        spotifyPlaylist = []

        users = UsersRepository().List()
        reviewsArtist = ResenhaRepository().List('artista')
        reviewsAlbum = ResenhaRepository().List('album')
        reviewsTrack = ResenhaRepository().List('track')
        reviewsPlaylist = ResenhaRepository().List('playlist')
        for item in reviews:
            if item.tipo_review == 'artista':
                spotifyArtist.append(
                    SpotifyGetOneArtist(item.spotify_id).oneArtist)
            elif item.tipo_review == 'album':
                spotifyAlbum.append(
                    SpotifyGetOneAlbum(item.spotify_id).oneAlbum)
            elif item.tipo_review == 'track':
                spotifyTrack.append(
                    SpotifyGetOneTrack(item.spotify_id).oneTrack)
            elif item.tipo_review == 'playlist':
                spotifyPlaylist.append(
                    SpotifyGetOnePlaylist(item.spotify_id).onePlaylist)

        return render_template('index.html', reviewsArtist=reviewsArtist, reviewsAlbum=reviewsAlbum,
                               reviewsTrack=reviewsTrack, reviewsPlaylist=reviewsPlaylist,
                               spotifyArtist=spotifyArtist, spotifyAlbum=spotifyAlbum,
                               spotifyTrack=spotifyTrack, spotifyPlaylist=spotifyPlaylist, users=users, mainFilter='index')


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
