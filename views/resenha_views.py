from flask import render_template, session, redirect, request, url_for, flash, Blueprint
from repository.users_repos import UsersRepository
from repository.resenha_repos import ResenhaRepository
from repository.comments_repos import CommentsRepository
from repository.curtidas_repos import CurtidasRepository
from models.common import DateConversion, KeepInSession, CleanSession
from thirdparty.spotify import SpotifyGetFiveArtists, SpotifyGetAlbums, \
    SpotifyGetOneArtist, SpotifyGetOneAlbum, SpotifyGetOneTrack, SpotifyGetOnePlaylist, \
    SpotifyGetPlaylists, SpotifyCheckUser, SpotifyGetTracks

res = Blueprint('res', __name__)


# <-- ## Artist routes beginning ## -->

@res.route('/resenhaListArtist', methods=['GET', 'POST'])
def resenhaListArtist():
    artists = SpotifyGetFiveArtists(request.form['artist']).listArtists

    if session['id'] != '':
        comments = CommentsRepository().listAuthorId(session['id'])
        likeNotifications = CurtidasRepository().listAuthorId(session['id'])
        usersNotifications = UsersRepository().List()
        resenhasListAll = ResenhaRepository().ListAll()

        return render_template('resenha/resenhaListArtist.html', artists=artists, comments=comments,
                               usersNotifications=usersNotifications, likeNotifications=likeNotifications,
                               resenhasListAll=resenhasListAll)
    else:
        return render_template('resenha/resenhaListArtist.html', artists=artists)


@res.route('/resenhaNewArtist/<artistId>/', methods=['GET', 'POST'])
def resenhaNewArtist(artistId):
    if session['email'] == '' or 'email' not in session:
        flash('Você precisa logar para acessar essa área', 'info')
        return redirect(url_for('log.login'))

    spotify = SpotifyGetOneArtist(artistId).createList()

    if session['id'] != '':
        comments = CommentsRepository().listAuthorId(session['id'])
        likeNotifications = CurtidasRepository().listAuthorId(session['id'])
        usersNotifications = UsersRepository().List()
        resenhasListAll = ResenhaRepository().ListAll()

        return render_template('resenha/resenhaNew.html', spotify=spotify, tipo_review='artista', comments=comments,
                               usersNotifications=usersNotifications, likeNotifications=likeNotifications,
                               resenhasListAll=resenhasListAll)
    else:
        return render_template('resenha/resenhaNew.html', spotify=spotify, tipo_review='artista')


@res.route('/createResenhaArtist', methods=['GET', 'POST'])
def createResenhaArtist():
    if session['email'] == '' or 'email' not in session:
        flash('Você precisa logar para acessar essa área', 'info')
        return redirect(url_for('log.login'))

    tipo_review = 'artista'
    author_id = session['id']
    nome_review = request.form['nome_review']
    spotify_id = request.form['spotify_id']
    review = request.form['review']

    # In case of error, review will be in session
    KeepInSession(request.form['spotify_id'],
                  request.form['nome_review'], request.form['review'])

    ResenhaRepository().New(tipo_review, author_id, nome_review, spotify_id, review)
    CleanSession()
    flash('Resenha criada com sucesso', 'success')
    return redirect(url_for('ind.home'))


# <-- ## Artists routes ending ## -->


# <-- ## Albums routes beginning ## -->
@res.route('/resenhalistAlbums/<artistId>/', methods=['GET', 'POST'])
def resenhalistAlbums(artistId):

    albums = SpotifyGetAlbums(artistId).createList()

    if session['id'] != '':
        comments = CommentsRepository().listAuthorId(session['id'])
        likeNotifications = CurtidasRepository().listAuthorId(session['id'])
        usersNotifications = UsersRepository().List()
        resenhasListAll = ResenhaRepository().ListAll()

        return render_template('resenha/resenhaListAlbums.html', albums=albums, comments=comments,
                               usersNotifications=usersNotifications, likeNotifications=likeNotifications,
                               resenhasListAll=resenhasListAll)
    else:
        return render_template('resenha/resenhaListAlbums.html', albums=albums)


@res.route('/resenhaNewAlbum/<albumId>/', methods=['GET', 'POST'])
def resenhaNewAlbum(albumId):
    if session['email'] == '' or 'email' not in session:
        flash('Você precisa logar para acessar essa área', 'info')
        return redirect(url_for('log.login'))

    spotify = SpotifyGetOneAlbum(albumId).createList()

    if session['id'] != '':
        comments = CommentsRepository().listAuthorId(session['id'])
        likeNotifications = CurtidasRepository().listAuthorId(session['id'])
        usersNotifications = UsersRepository().List()
        resenhasListAll = ResenhaRepository().ListAll()

        return render_template('resenha/resenhaNew.html', spotify=spotify, tipo_review='album', comments=comments,
                               usersNotifications=usersNotifications, likeNotifications=likeNotifications,
                               resenhasListAll=resenhasListAll)

    else:
        return render_template('resenha/resenhaNew.html', spotify=spotify, tipo_review='album')


# <-- ## Albums routes ending ## -->


# <-- ## Tracks routes beginning ## -->

@res.route('/resenhaListTracks', methods=['GET', 'POST'])
def resenhaListTracks():
    tracks = SpotifyGetTracks(request.form['spotifyTracks']).createList()

    if session['id'] != '':
        comments = CommentsRepository().listAuthorId(session['id'])
        likeNotifications = CurtidasRepository().listAuthorId(session['id'])
        usersNotifications = UsersRepository().List()
        resenhasListAll = ResenhaRepository().ListAll()

        return render_template('resenha/resenhaListTracks.html', tracks=tracks, comments=comments,
                               usersNotifications=usersNotifications, likeNotifications=likeNotifications,
                               resenhasListAll=resenhasListAll)
    else:
        return render_template('resenha/resenhaListTracks.html', tracks=tracks)


@res.route('/resenhaNewTrack/<trackId>/', methods=['GET', 'POST'])
def resenhaNewTrack(trackId):
    if session['email'] == '' or 'email' not in session:
        flash('Você precisa logar para acessar essa área', 'info')
        return redirect(url_for('log.login'))

    spotify = SpotifyGetOneTrack(trackId).createList()

    if session['id'] != '':
        comments = CommentsRepository().listAuthorId(session['id'])
        likeNotifications = CurtidasRepository().listAuthorId(session['id'])
        usersNotifications = UsersRepository().List()
        resenhasListAll = ResenhaRepository().ListAll()

        return render_template('resenha/resenhaNew.html', spotify=spotify, tipo_review='track', comments=comments,
                               usersNotifications=usersNotifications, likeNotifications=likeNotifications,
                               resenhasListAll=resenhasListAll)
    else:
        return render_template('resenha/resenhaNew.html', spotify=spotify, tipo_review='track')


# <-- ## Playlists routes beginning ## -->

@res.route('/resenhaListPlaylists', methods=['GET', 'POST'])
def resenhaListPlaylists():
        try:
            SpotifyCheckUser(request.form['spotifyUsername'])
            playlists = SpotifyGetPlaylists(request.form['spotifyUsername']).createList()

            if session['id'] != '':
                comments = CommentsRepository().listAuthorId(session['id'])
                likeNotifications = CurtidasRepository().listAuthorId(session['id'])
                usersNotifications = UsersRepository().List()
                resenhasListAll = ResenhaRepository().ListAll()
                return render_template('resenha/resenhaListPlaylists.html', playlists=playlists, comments=comments,
                               usersNotifications=usersNotifications, likeNotifications=likeNotifications,
                               resenhasListAll=resenhasListAll)
            else:
                return render_template('resenha/resenhaListPlaylists.html', playlists=playlists)
        except:
            flash('Nome de usuário não encontrado', 'danger')
            return redirect(url_for('res.resenhaIndex'))


@res.route('/resenhaNewPlaylist/<playlistId>/', methods=['GET', 'POST'])
def resenhaNewPlaylist(playlistId):
    if session['email'] == '' or 'email' not in session:
        flash('Você precisa logar para acessar essa área', 'info')
        return redirect(url_for('log.login'))

    spotify = SpotifyGetOnePlaylist(playlistId).createList()

    if session['id'] != '':
        comments = CommentsRepository().listAuthorId(session['id'])
        likeNotifications = CurtidasRepository().listAuthorId(session['id'])
        usersNotifications = UsersRepository().List()
        resenhasListAll = ResenhaRepository().ListAll()

        return render_template('resenha/resenhaNew.html', spotify=spotify, tipo_review='playlist', comments=comments,
                               usersNotifications=usersNotifications, likeNotifications=likeNotifications,
                               resenhasListAll=resenhasListAll)
    else:
        return render_template('resenha/resenhaNew.html', spotify=spotify, tipo_review='playlist')


@res.route('/createResenhaPlaylist', methods=['GET', 'POST'])
def createResenhaPlaylist():
    if session['email'] == '' or 'email' not in session:
        flash('Você precisa logar para acessar essa área', 'info')
        return redirect(url_for('log.login'))

    tipo_review = 'playlist'
    author_id = session['id']
    nome_review = request.form['nome_review']
    spotify_id = request.form['spotify_id']
    review = request.form['review']

    # In case of error, review will be in session
    KeepInSession(request.form['spotify_id'],
                  request.form['nome_review'], request.form['review'])

    ResenhaRepository().New(tipo_review, author_id, nome_review, spotify_id, review)
    CleanSession()
    flash('Resenha criada com sucesso', 'success')
    return redirect(url_for('ind.home'))


# <-- ## Playlists routes ending ## -->


# <-- ## Other routes beginning ## -->
@res.route('/resenhaIndex', methods=['GET', 'POST'])
def resenhaIndex():
    CleanSession()
    if session['email'] == '' or 'email' not in session:
        session['previous'] = 'res.resenhaIndex'
        flash('Você precisa logar para acessar essa área', 'info')
        return redirect(url_for('log.login'))

    if session['id'] != '':
        comments = CommentsRepository().listAuthorId(session['id'])
        likeNotifications = CurtidasRepository().listAuthorId(session['id'])
        usersNotifications = UsersRepository().List()
        resenhasListAll = ResenhaRepository().ListAll()

        return render_template('resenha/resenhaIndex.html', comments=comments, usersNotifications=usersNotifications,
                               likeNotifications=likeNotifications, resenhasListAll=resenhasListAll)
    else:
        return render_template('resenha/resenhaIndex.html')


@res.route('/createResenha', methods=['GET', 'POST'])
def createResenha():
    if session['email'] == '' or 'email' not in session:
        flash('Você precisa logar para acessar essa área', 'info')
        return redirect(url_for('log.login'))

    tipo_review = request.form['tipo_review']
    author_id = session['id']
    nome_review = request.form['nome_review']
    spotify_id = request.form['spotify_id']
    review = request.form['review']

    # In case of error, review will be in session
    KeepInSession(request.form['spotify_id'],
                  request.form['nome_review'], request.form['review'])

    ResenhaRepository().New(tipo_review, author_id, nome_review, spotify_id, review)
    CleanSession()
    flash('Resenha criada com sucesso', 'success')
    return redirect(url_for('ind.home'))


@res.route('/resenhaEdit/<int:id>', methods=['GET', 'POST'])
def resenhaEdit(id):
    data = ResenhaRepository().FindById(id)
    spotifyId = data.spotify_id
    if data.tipo_review == 'artista':
        spotify = SpotifyGetOneArtist(spotifyId).oneArtist
    elif data.tipo_review == 'album':
        spotify = SpotifyGetOneAlbum(spotifyId).oneAlbum
    elif data.tipo_review == 'track':
        spotify = SpotifyGetOneTrack(spotifyId).oneTrack
    else:
        spotify = SpotifyGetOnePlaylist(spotifyId).onePlaylist

    if session['id'] != data.author_id:
        return redirect(url_for('ind.home'))
    else:
        voltarButton = request.headers.get("Referer")

        if session['id'] != '':
            comments = CommentsRepository().listAuthorId(session['id'])
            likeNotifications = CurtidasRepository().listAuthorId(session['id'])
            usersNotifications = UsersRepository().List()
            resenhasListAll = ResenhaRepository().ListAll()

            return render_template('resenha/resenhaEdit.html', data=data, spotify=spotify, voltarButton=voltarButton,
                                   comments=comments, usersNotifications=usersNotifications,
                               likeNotifications=likeNotifications, resenhasListAll=resenhasListAll)
        else:
            return render_template('resenha/resenhaEdit.html', data=data, spotify=spotify, voltarButton=voltarButton)


@res.route('/updateResenha', methods=['GET', 'POST'])
def updateResenha():
    id = request.form['id']
    nome_review = str(request.form['nome_review'])
    review = request.form['review']

    ResenhaRepository().Edit(id, nome_review, review)
    flash('Resenha atualizada com sucesso', 'success')

    return redirect(url_for('res.resenhado', id=id))


@res.route('/resenhado/<id>/')
def resenhado(id):

    if 'id' not in session:
        session['id'] = ''

    data = ResenhaRepository().FindById(id)
    spotifyId = data.spotify_id
    if data.tipo_review == 'artista':
        spotify = SpotifyGetOneArtist(spotifyId).oneArtist
    elif data.tipo_review == 'album':
        spotify = SpotifyGetOneAlbum(spotifyId).oneAlbum
    elif data.tipo_review == 'track':
        spotify = SpotifyGetOneTrack(spotifyId).oneTrack
    else:
        spotify = SpotifyGetOnePlaylist(spotifyId).onePlaylist

    user_author = UsersRepository().FindById(data.author_id)
    date = DateConversion(str(data.date_register))

    like = CurtidasRepository().CountLikes(id).count

    commentsList = CommentsRepository().List(id)
    comment_user = UsersRepository().List()

    try:
        if CurtidasRepository().FindById(session['id'], id):
            PNG = 'unclick'
        else:
            PNG = 'click'
    except:
        PNG = 'click'

    if session['id'] != '':
        comments = CommentsRepository().listAuthorId(session['id'])
        likeNotifications = CurtidasRepository().listAuthorId(session['id'])
        usersNotifications = UsersRepository().List()
        resenhasListAll = ResenhaRepository().ListAll()

        return render_template('resenha/resenhado.html', data=data, spotify=spotify, user_author=user_author, date=date,
                               commentsList=commentsList, comment_user=comment_user, like=like, PNG=PNG,
                               comments=comments, usersNotifications=usersNotifications,
                               likeNotifications=likeNotifications, resenhasListAll=resenhasListAll)

    else:
        return render_template('resenha/resenhado.html', data=data, spotify=spotify, user_author=user_author, date=date,
                               commentsList=commentsList, comment_user=comment_user, like=like, PNG=PNG)
