from flask import render_template, session, redirect, request, url_for, flash, Blueprint
from repository.users_repos import UsersRepository
from repository.resenha_repos import ResenhaRepository
from repository.comments_repos import CommentsRepository
from models.common import DateConversion
from thirdparty.spotify import SpotifyLink, SpotifyImage, SpotifyTipoResenha
from datetime import date

res = Blueprint('res', __name__)


# <--- 'Resenha' routes beginning --->

@res.route('/nova_resenha', methods=['GET', 'POST'])
def nova_resenha():
    if session['username'] == '' or 'username' not in session:
        flash('Você precisa logar para acessar essa área', 'danger')
        return redirect(url_for('ind.home'))

    flash('!!!IMPORTANTE!!! Sem um link do Spotify, sua resenha NÃO irá ao ar.', 'warning')
    return render_template('nova_resenha.html')


@res.route('/criar_resenha', methods=['GET', 'POST'])
def criar_resenha():
    if session['username'] == '' or 'username' not in session:
        flash('Você precisa logar para acessar essa área', 'danger')
        return redirect(url_for('ind.home'))

    tipo_review = str(SpotifyTipoResenha(str(request.form['spotify_link'])))
    author_id = session['id']
    spotify_link = str(SpotifyLink(str(request.form['spotify_link'])))

    if '' == spotify_link:
        flash('Link do Spotify invalido', 'danger')
        return render_template('nova_resenha.html')

    nome_review = request.form['nome_review']
    nome_banda = request.form['nome_banda']
    review = request.form['review']
    date_register = date.today()
    filename = str(SpotifyImage(str(request.form['spotify_link'])))

    ResenhaRepository().New(tipo_review, author_id, spotify_link,
                            nome_review, nome_banda, review, date_register, filename)

    return redirect(url_for('ind.home'))


@res.route('/editar_resenha/<int:id>', methods=['GET', 'POST'])
def editar_resenha(id):
    resenha = ResenhaRepository().FindById(id)
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

    nome_review = request.form['nome_review']
    nome_banda = request.form['nome_banda']
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

    comments = CommentsRepository().List(id)
    comment_user = UsersRepository().List()

    return render_template('resenhado.html', data=data, user_author=user_author,
        date=date, comments=comments, comment_user=comment_user)


@res.route('/home/<int:id>/')
def minhas_resenhas(id):
    if session['username'] == '' or 'username' not in session:
        flash('Você precisa logar para acessar essa área', 'danger')
        return redirect(url_for('ind.home'))

    resenhas = ResenhaRepository().FindAuthorById(id)
    if not resenhas:
        flash('Você ainda não criou nenhuma resenha', 'info')
    else:
        flash('Essas são as resenhas criadas por você até o momento', 'info')
    return render_template('index.html', resenhas=resenhas)

