from flask import render_template, session, redirect, request, url_for, flash, Blueprint
from repository.users_repos import UsersRepository
from repository.resenha_repos import ResenhaRepository
from repository.comments_repos import CommentsRepository
from repository.curtidas_repos import CurtidasRepository
from models.common import DateConversion, KeepInSession, CleanSession
from thirdparty.spotify import SpotifyLink, SpotifyImage, SpotifyTipoResenha
from datetime import date

res = Blueprint('res', __name__)


@res.route('/nova_resenha', methods=['GET', 'POST'])
def nova_resenha():
    CleanSession()
    if session['username'] == '' or 'username' not in session:
        flash('Você precisa logar para acessar essa área', 'danger')
        return redirect(url_for('ind.home'))

    flash('!!!IMPORTANTE!!! Sem um link do Spotify, sua resenha NÃO irá ao ar.', 'warning')
    return render_template('teste.html')


@res.route('/criar_resenha', methods=['GET', 'POST'])
def criar_resenha():
    if session['username'] == '' or 'username' not in session:
        flash('Você precisa logar para acessar essa área', 'info')
        return redirect(url_for('log.login'))

    tipo_review = str(SpotifyTipoResenha(str(request.form['spotify_link'])))
    author_id = session['id']
    spotify_link = str(SpotifyLink(str(request.form['spotify_link'])))

    KeepInSession(request.form['nome_review'],
                  request.form['nome_banda'], request.form['review'])

    if '' == spotify_link:
        flash('Link do Spotify invalido', 'danger')
        return render_template('teste.html')

    nome_review = request.form['nome_review']
    nome_banda = request.form['nome_banda']
    review = request.form['review']
    date_register = date.today()
    filename = str(SpotifyImage(str(request.form['spotify_link'])))

    ResenhaRepository().New(tipo_review, author_id, spotify_link,
                            nome_review, nome_banda, review, date_register, filename)
    CleanSession()
    flash('Resenha criada com sucesso', 'success')
    return redirect(url_for('ind.home'))


@res.route('/editar_resenha/<int:id>', methods=['GET', 'POST'])
def editar_resenha(id):
    resenha = ResenhaRepository().FindById(id)
    if session['id'] != resenha.author_id:
        return redirect(url_for('ind.home'))
    else:
        flash('!!!IMPORTANTE!!!   Sem um link do Spotify, sua resenha NÃO irá ao ar.', 'warning')
        return render_template('editar_resenha.html', resenha=resenha)


@res.route('/atualizar_resenha', methods=['GET', 'POST'])
def atualizar_resenha():
    id = request.form['id']
    tipo_review = str(SpotifyTipoResenha(str(request.form['spotify_link'])))
    spotify_link = str(SpotifyLink(str(request.form['spotify_link'])))

    if '' == spotify_link:
        resenha = ResenhaRepository().FindById(id)
        flash('Link do Spotify inválido', 'danger')
        return render_template('editar_resenha.html', resenha=resenha)

    nome_review = str(request.form['nome_review'])
    nome_banda = str(request.form['nome_banda'])
    review = request.form['review']
    date_register = date.today()
    filename = str(SpotifyImage(str(request.form['spotify_link'])))

    ResenhaRepository().Edit(id, tipo_review, spotify_link, nome_review,
                             nome_banda, review, date_register, filename)
    flash('Resenha atualizada com sucesso', 'success')
    return redirect(url_for('res.minhas_resenhas', id=session['id']))


@res.route('/resenhado/<int:id>/')
def resenhado(id):
    data = ResenhaRepository().FindById(id)
    user_author = UsersRepository().FindById(data.author_id)
    date = DateConversion(str(data.date_register))

    like = CurtidasRepository().CountLikes(id).count

    comments = CommentsRepository().List(id)
    comment_user = UsersRepository().List()

    if CurtidasRepository().FindById(session['id'], id):
        PNG = 'unclick'
    else:
        PNG = 'click'

    return render_template('resenhado.html', data=data, user_author=user_author,
                           date=date, comments=comments, comment_user=comment_user,
                           like=like, PNG=PNG)


@res.route('/home/<int:id>/')
def minhas_resenhas(id):

    resenhas = ResenhaRepository().FindAuthorById(id)
    if not resenhas:
        flash('Você ainda não criou nenhuma resenha', 'info')
    else:
        flash('Essas são as resenhas criadas por você até o momento', 'info')
    return render_template('teste.html', resenhas=resenhas)
