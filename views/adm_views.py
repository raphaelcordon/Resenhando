from flask import render_template, redirect, url_for, flash, Blueprint
from repository.users_repos import UsersRepository
from repository.resenha_repos import ResenhaRepository

adm = Blueprint('adm', __name__)

# <--- ADMINISTRATIVE routes beginning --->

@adm.route('/adm_resenhas')
def adm_resenhas():
    resenhas = ResenhaRepository().List()
    return render_template('_adm_resenhas.html', resenhas=resenhas)


@adm.route('/UsuariosDelete/<int:user_id>')
def UsuariosDelete(user_id):
    UsersRepository().Delete(user_id)
    flash('Usuario Successfully removed', 'info')
    return redirect(url_for('use.usuarios'))


@adm.route('/sobre')
def sobre():
    return render_template('sobre.html')