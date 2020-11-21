from flask import render_template, session, redirect, url_for, Blueprint, flash
from thirdparty.spotify import SpotifyGetOneAlbum, SpotifyGetOneArtist, SpotifyGetOneTrack, SpotifyGetOnePlaylist
from repository.users_repos import UsersRepository
from repository.resenha_repos import ResenhaRepository
from repository.comments_repos import CommentsRepository
from repository.curtidas_repos import CurtidasRepository
from models import genres_model

filter = Blueprint('filter', __name__, url_prefix='')

"""
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

    if session['id'] != '':
        comments = CommentsRepository().listAuthorId(session['id'])
        likeNotifications = CurtidasRepository().listAuthorId(session['id'])
        usersNotifications = UsersRepository().List()
        resenhasListAll = ResenhaRepository().ListAll()
        notifyComment = UsersRepository().FindById(session['id']).read_comment
        notifyLike = UsersRepository().FindById(session['id']).read_like

        return render_template('resenha/resenhaViews.html', reviewsArtist=reviewsArtist, reviewsAlbum=reviewsAlbum,
                               reviewsTrack=reviewsTrack, reviewsPlaylist=reviewsPlaylist,
                               users=users, spotifyArtist=spotifyArtist, spotifyAlbum=spotifyAlbum,
                               spotifyTrack=spotifyTrack, spotifyPlaylist=spotifyPlaylist, mainFilter='everything',
                               comments=comments, usersNotifications=usersNotifications,
                               likeNotifications=likeNotifications, resenhasListAll=resenhasListAll,
                               notifyComment=notifyComment, notifyLike=notifyLike)
    else:
        return render_template('resenha/resenhaViews.html', reviewsArtist=reviewsArtist, reviewsAlbum=reviewsAlbum,
                               reviewsTrack=reviewsTrack, reviewsPlaylist=reviewsPlaylist,
                               users=users, spotifyArtist=spotifyArtist, spotifyAlbum=spotifyAlbum,
                               spotifyTrack=spotifyTrack, spotifyPlaylist=spotifyPlaylist, mainFilter='everything')
"""# Everything, is inactivated, just available as reference


@filter.route('/filterArtist')
def filterArtist():

    if 'id' not in session:
        session['id'] = ''

    spotifyArtist = []

    users = UsersRepository().List()
    reviewsArtist = ResenhaRepository().List('artista')

    for item in reviewsArtist:
        spotifyArtist.append(SpotifyGetOneArtist(item.spotify_id).oneArtist)

    if session['id'] != '':
        comments = CommentsRepository().listAuthorId(session['id'])
        likeNotifications = CurtidasRepository().listAuthorId(session['id'])
        usersNotifications = UsersRepository().List()
        resenhasListAll = ResenhaRepository().ListAll()
        notifyComment = UsersRepository().FindById(session['id']).read_comment
        notifyLike = UsersRepository().FindById(session['id']).read_like

        return render_template('filters/filterArtists.html', reviewsArtist=reviewsArtist, spotifyArtist=spotifyArtist,
                               users=users, comments=comments, notifyComment=notifyComment, notifyLike=notifyLike,
                               usersNotifications=usersNotifications, likeNotifications=likeNotifications,
                               resenhasListAll=resenhasListAll)

    else:
        return render_template('filters/filterArtists.html', reviewsArtist=reviewsArtist, spotifyArtist=spotifyArtist,
                               users=users)


@filter.route('/filterAlbum')
def filterAlbum():

    if 'id' not in session:
        session['id'] = ''

    spotifyAlbum = []

    users = UsersRepository().List()
    reviewsAlbum = ResenhaRepository().List('album')
    for item in reviewsAlbum:
        spotifyAlbum.append(SpotifyGetOneAlbum(item.spotify_id).oneAlbum)

    if session['id'] != '':
        comments = CommentsRepository().listAuthorId(session['id'])
        likeNotifications = CurtidasRepository().listAuthorId(session['id'])
        usersNotifications = UsersRepository().List()
        resenhasListAll = ResenhaRepository().ListAll()
        notifyComment = UsersRepository().FindById(session['id']).read_comment
        notifyLike = UsersRepository().FindById(session['id']).read_like

        return render_template('filters/filterAlbums.html', reviewsAlbum=reviewsAlbum, spotifyAlbum=spotifyAlbum,
                               users=users, comments=comments, notifyComment=notifyComment, notifyLike=notifyLike,
                               usersNotifications=usersNotifications, likeNotifications=likeNotifications,
                               resenhasListAll=resenhasListAll)
    else:
        return render_template('filters/filterAlbums.html', reviewsAlbum=reviewsAlbum, spotifyAlbum=spotifyAlbum,
                               users=users)


@filter.route('/filterTrack')
def filterTrack():

    if 'id' not in session:
        session['id'] = ''

    spotifyTrack = []

    users = UsersRepository().List()
    reviewsTrack = ResenhaRepository().List('track')
    for item in reviewsTrack:
        spotifyTrack.append(SpotifyGetOneTrack(item.spotify_id).oneTrack)

    if session['id'] != '':
        comments = CommentsRepository().listAuthorId(session['id'])
        likeNotifications = CurtidasRepository().listAuthorId(session['id'])
        usersNotifications = UsersRepository().List()
        resenhasListAll = ResenhaRepository().ListAll()
        notifyComment = UsersRepository().FindById(session['id']).read_comment
        notifyLike = UsersRepository().FindById(session['id']).read_like

        return render_template('filters/filterTracks.html', reviewsTrack=reviewsTrack, spotifyTrack=spotifyTrack,
                               users=users, comments=comments, notifyComment=notifyComment, notifyLike=notifyLike,
                               usersNotifications=usersNotifications, likeNotifications=likeNotifications,
                               resenhasListAll=resenhasListAll)
    else:
        return render_template('filters/filterTracks.html', reviewsTrack=reviewsTrack, spotifyTrack=spotifyTrack,
                               users=users)


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

    if session['id'] != '':
        comments = CommentsRepository().listAuthorId(session['id'])
        likeNotifications = CurtidasRepository().listAuthorId(session['id'])
        usersNotifications = UsersRepository().List()
        resenhasListAll = ResenhaRepository().ListAll()
        notifyComment = UsersRepository().FindById(session['id']).read_comment
        notifyLike = UsersRepository().FindById(session['id']).read_like

        return render_template('filters/filterPlaylists.html', reviewsPlaylist=reviewsPlaylist,
                               spotifyPlaylist=spotifyPlaylist, users=users, comments=comments,
                               notifyComment=notifyComment, notifyLike=notifyLike,
                               usersNotifications=usersNotifications, likeNotifications=likeNotifications,
                               resenhasListAll=resenhasListAll)
    else:
        return render_template('filters/filterPlaylists.html', reviewsPlaylist=reviewsPlaylist,
                               spotifyPlaylist=spotifyPlaylist, users=users)


@filter.route('/<int:id>/')
def minhas_resenhas(id):
    if session['email'] == '' or 'email' not in session or session['id'] == '':
        flash('Você precisa logar para acessar essa área', 'info')
        return redirect(url_for('log.login'))

    if 'id' not in session:
        session['id'] = ''

    reviews = ResenhaRepository().FindAuthorById(id)
    user = UsersRepository().FindById(id)

    if not reviews:
        flash('Você ainda não criou nenhuma resenha', 'info')
        return redirect(url_for('ind.home'))
    else:
        return redirect(url_for('filter.myPage', name=str(user.name).lower(), surname=str(user.surname).lower()))


@filter.route('/genresBody/<genreLink>')
def genresBody(genreLink):

    if 'id' not in session:
        session['id'] = ''

    genreLink = genreLink
    users = UsersRepository().List()
    genres = genres_model.genres
    resenhasListAll = ResenhaRepository().ListAll()
    spotifyArtist = []
    spotifyAlbum = []
    spotifyTrack = []

    reviewsArtist = ResenhaRepository().ListOneGenre('artista', genreLink)
    for item in reviewsArtist:
        print(item.genre)
    reviewsAlbum = ResenhaRepository().ListOneGenre('album', genreLink)
    reviewsTrack = ResenhaRepository().ListOneGenre('track', genreLink)
    for item in reviewsArtist:
        spotifyArtist.append(SpotifyGetOneArtist(item.spotify_id).oneArtist)
    for item in reviewsAlbum:
        spotifyAlbum.append(SpotifyGetOneAlbum(item.spotify_id).oneAlbum)
    for item in reviewsTrack:
        spotifyTrack.append(SpotifyGetOneTrack(item.spotify_id).oneTrack)

    genreCount = {}
    for item in genres:
        count = 0
        for genre in resenhasListAll:
            if genre.genre == item:
                count += 1
        if count > 0:
            genreCount[item] = count

    if session['id'] != '':
        comments = CommentsRepository().listAuthorId(session['id'])
        likeNotifications = CurtidasRepository().listAuthorId(session['id'])
        usersNotifications = UsersRepository().List()
        notifyComment = UsersRepository().FindById(session['id']).read_comment
        notifyLike = UsersRepository().FindById(session['id']).read_like

        return render_template('filters/genresBody.html', users=users, reviewsArtist=reviewsArtist,
                               reviewsAlbum=reviewsAlbum, reviewsTrack=reviewsTrack,
                               spotifyArtist=spotifyArtist, spotifyAlbum=spotifyAlbum, spotifyTrack=spotifyTrack,
                               comments=comments, usersNotifications=usersNotifications,
                               likeNotifications=likeNotifications, notifyComment=notifyComment,
                               notifyLike=notifyLike, genres=genres, genreCount=genreCount, genreLink=genreLink)
    else:
        return render_template('filters/genresBody.html', users=users, reviewsArtist=reviewsArtist,
                               reviewsAlbum=reviewsAlbum, reviewsTrack=reviewsTrack,
                               spotifyArtist=spotifyArtist, spotifyAlbum=spotifyAlbum,
                               spotifyTrack=spotifyTrack, genres=genres, genreCount=genreCount, genreLink=genreLink)


@filter.route('/filterGenres/')
def filterGenres():

    if 'id' not in session:
        session['id'] = ''

    genres = genres_model.genres
    resenhasListAll = ResenhaRepository().ListAll()

    genreCount = {}
    for item in genres:
        count = 0
        for genre in resenhasListAll:
            if genre.genre == item:
                count += 1
        if count > 0:
            genreCount[item] = count

    return render_template('filters/filterGenres.html', genres=genres, genreCount=genreCount)


@filter.route('/<name>-<surname>/')
def myPage(name, surname):

    if 'id' not in session:
        session['id'] = ''

    try:
        authorID = ResenhaRepository().FindAuthorByNameSurname(str(name).title(), str(surname).title()).id
        if not authorID:
            return redirect(url_for('ind.home'))

        reviews = ResenhaRepository().FindAuthorById(authorID)
        if not reviews:

            flash(f'{str(name).title()} {str(surname).title()} ainda não criou resenhas', 'info')
            return redirect(url_for('ind.home'))
        else:
            flash(f'Resenhas de {str(name).title()} {str(surname).title()}: '
                  f"   resenhando.co/{str(name).lower()}-{str(surname).lower()}   ", 'info')

            spotifyArtist = []
            spotifyAlbum = []
            spotifyTrack = []
            spotifyPlaylist = []
            reviewsArtist = []
            reviewsAlbum = []
            reviewsTrack = []
            reviewsPlaylist = []

            users = UsersRepository().List()
            for item in reviews:
                if item.tipo_review == 'artista':
                    reviewsArtist.append(item)
                elif item.tipo_review == 'album':
                    reviewsAlbum.append(item)
                elif item.tipo_review == 'track':
                    reviewsTrack.append(item)
                elif item.tipo_review == 'playlist':
                    reviewsPlaylist.append(item)

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

            if session['id'] != '':
                comments = CommentsRepository().listAuthorId(session['id'])
                likeNotifications = CurtidasRepository().listAuthorId(session['id'])
                usersNotifications = UsersRepository().List()
                resenhasListAll = ResenhaRepository().ListAll()
                notifyComment = UsersRepository().FindById(session['id']).read_comment
                notifyLike = UsersRepository().FindById(session['id']).read_like

                return render_template('resenha/resenhaViews.html', reviewsArtist=reviewsArtist, reviewsAlbum=reviewsAlbum,
                                       reviewsTrack=reviewsTrack, reviewsPlaylist=reviewsPlaylist,
                                       users=users, spotifyArtist=spotifyArtist, spotifyAlbum=spotifyAlbum,
                                       spotifyTrack=spotifyTrack, spotifyPlaylist=spotifyPlaylist, mainFilter='myPage',
                                       comments=comments, usersNotifications=usersNotifications,
                                       likeNotifications=likeNotifications, resenhasListAll=resenhasListAll,
                                       notifyComment=notifyComment, notifyLike=notifyLike)

            else:
                return render_template('index.html', reviewsArtist=reviewsArtist, reviewsAlbum=reviewsAlbum,
                                       reviewsTrack=reviewsTrack, reviewsPlaylist=reviewsPlaylist,
                                       users=users, spotifyArtist=spotifyArtist, spotifyAlbum=spotifyAlbum,
                                       spotifyTrack=spotifyTrack, spotifyPlaylist=spotifyPlaylist, mainFilter='myPage')

    except:
        flash('Usuário não identificado', 'danger')
        return redirect(url_for('ind.home'))


@filter.route('/blank')# Initial page for filterGenres.html
def blank():
    return render_template('filters/blank.html')


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
