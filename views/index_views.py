from flask import render_template, session, redirect, url_for, Blueprint, Response
from thirdparty.spotify import SpotifyGetOneAlbum, SpotifyGetOneArtist, SpotifyGetOneTrack, SpotifyGetOnePlaylist
from repository.users_repos import UsersRepository
from repository.resenha_repos import ResenhaRepository
from repository.comments_repos import CommentsRepository
from repository.curtidas_repos import CurtidasRepository

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

    if session['id'] != '':
        comments = CommentsRepository().listAuthorId(session['id'])
        likeNotifications = CurtidasRepository().listAuthorId(session['id'])
        usersNotifications = UsersRepository().List()
        resenhasListAll = ResenhaRepository().ListAll()
        notifyComment = UsersRepository().FindById(session['id']).read_comment
        notifyLike = UsersRepository().FindById(session['id']).read_like

        return render_template('index.html', reviewsArtist=reviewsArtist, reviewsAlbum=reviewsAlbum,
                               reviewsTrack=reviewsTrack, reviewsPlaylist=reviewsPlaylist,
                               users=users, spotifyArtist=spotifyArtist, spotifyAlbum=spotifyAlbum,
                               spotifyTrack=spotifyTrack, spotifyPlaylist=spotifyPlaylist, mainFilter='index',
                               comments=comments, usersNotifications=usersNotifications,
                               likeNotifications=likeNotifications, resenhasListAll=resenhasListAll,
                               notifyComment=notifyComment, notifyLike=notifyLike)
    else:
        return render_template('index.html', reviewsArtist=reviewsArtist, reviewsAlbum=reviewsAlbum,
                               reviewsTrack=reviewsTrack, reviewsPlaylist=reviewsPlaylist,
                               users=users, spotifyArtist=spotifyArtist, spotifyAlbum=spotifyAlbum,
                               spotifyTrack=spotifyTrack, spotifyPlaylist=spotifyPlaylist, mainFilter='index')


@ind.route('/home/')
def home():

    return redirect(url_for('ind.index'))


@ind.route('/<ads>.<txt>')
def adsTxt(ads, txt):
    if ads == 'ads' and txt == 'txt':
        with open("ads.txt", "r") as f:
            content = f.read()
        return Response(content, mimetype='text/plain')
    else:
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
    session['lastURL'] = ''
