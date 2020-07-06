from flask import session, redirect, url_for, Blueprint, flash
from repository.curtidas_repos import CurtidasRepository

cur = Blueprint('cur', __name__)


@cur.route('/curtida/<int:resenha_id>', methods=['GET', 'POST'])
def curtida(resenha_id):
    if session['username'] == '' or 'username' not in session:
        flash('Você precisa logar para acessar essa área', 'info')
        return redirect(url_for('log.login'))

    if CurtidasRepository().FindById(session['id'], resenha_id):
        CurtidasRepository().Delete(session['id'], resenha_id)
    else:
        CurtidasRepository().New(session['id'], resenha_id)
    return redirect(url_for('res.resenhado', id=resenha_id))
