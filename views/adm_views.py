from flask import render_template, redirect, url_for, flash, Blueprint
from repository.users_repos import UsersRepository
from repository.resenha_repos import ResenhaRepository

adm = Blueprint('adm', __name__)

# <--- ADMINISTRATIVE routes beginning --->

@adm.route('/usuarios')
def usuarios():
    users_list = UsersRepository().List()
    return render_template('_usuarios.html', users=users_list)


@adm.route('/UsuariosDelete/<int:user_id>')
def UsuariosDelete(user_id):
    UsersRepository().Delete(user_id)
    flash('Usuario Successfully removed', 'info')
    return redirect(url_for('adm.usuarios'))


@adm.route('/adm_resenhas')
def adm_resenhas():
    resenhas = ResenhaRepository().List()
    return render_template('_adm_resenhas.html', resenhas=resenhas)


@adm.route('/ResenhasDelete/<int:resenha_id>')
def ResenhasDelete(resenha_id):
    ResenhaRepository().Delete(resenha_id)
    flash('Resenha Successfully removed', 'info')
    return redirect(url_for('adm.adm_resenhas'))


@adm.route('/sobre')
def sobre():
    return render_template('sobre.html')