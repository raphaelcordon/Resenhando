from flask import render_template, redirect, url_for, flash, Blueprint, request
from repository.users_repos import UsersRepository
from repository.resenha_repos import ResenhaRepository
from repository.comments_repos import CommentsRepository

adm = Blueprint('adm', __name__)


@adm.route('/_adm')
def _adm():
    return render_template('_adm.html')


@adm.route('/adm_resenhas')
def adm_resenhas():
    resenhas = ResenhaRepository().List()
    return render_template('_adm_resenhas.html', resenhas=resenhas)


@adm.route('/adm_usuarios')
def adm_usuarios():
    users_list = UsersRepository().List()
    return render_template('_adm_usuarios.html', users=users_list)


@adm.route('/UsuariosDelete/<int:user_id>')
def UsuariosDelete(user_id):
    UsersRepository().Delete(user_id)
    flash('Usuario Successfully removed', 'info')
    return redirect(url_for('adm.adm_usuarios'))


@adm.route('/ResenhasDelete/<int:resenha_id>')
def ResenhasDelete(resenha_id):
    CommentsRepository().DeleteAllComments(resenha_id)
    ResenhaRepository().Delete(resenha_id)
    flash('Resenha Successfully removed', 'info')
    return redirect(url_for('adm.adm_resenhas'))


@adm.route('/adm_UsersRegistry', methods=['POST', ])
def adm_users_registry():
    email = str(request.form['email']).strip().lower()
    name = str(request.form['name']).strip().title()
    surname = str(request.form['surname']).strip().title()

    if email == '' or name == '' or surname == '':
        flash('Blank field not accepted', 'info')
    elif UsersRepository().New(name, surname, 'pass', email):
        flash('Already registered, please check below', 'info')
    else:
        flash(
            "Conta criada com sucesso. Utilize a senha 'pass' no primeiro login.", 'success')
    return redirect(url_for('use._adm_usuarios'))


@adm.route('/sobre')
def sobre():
    return render_template('sobre.html')
