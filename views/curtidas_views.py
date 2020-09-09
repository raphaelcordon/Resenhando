from flask import session, redirect, url_for, Blueprint, flash
from repository.curtidas_repos import CurtidasRepository
from repository.resenha_repos import ResenhaRepository

cur = Blueprint('cur', __name__)


@cur.route('/curtida/<int:resenha_id>', methods=['GET', 'POST'])
def curtida(resenha_id):

    if 'email' not in session:
        session['email'] = ''

    if session['email'] == '' or 'email' not in session:
        flash('Você precisa logar para acessar essa área', 'info')
        return redirect(url_for('log.login'))

    if CurtidasRepository().FindById(session['id'], resenha_id):
        CurtidasRepository().Delete(session['id'], resenha_id)
    else:
        CurtidasRepository().New(session['id'], resenha_id)
        authorID = ResenhaRepository().FindById(resenha_id).author_id
        CurtidasRepository().LikeNew(authorID)
    return redirect(url_for('res.resenhado', id=resenha_id))


@cur.route('/likeRead/')
def commentRead():
    CurtidasRepository().LikeRead(session['id'])