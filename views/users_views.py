from flask import redirect, request, url_for, flash, Blueprint, session, render_template
from repository.users_repos import UsersRepository
from models.common import CleanLoginItens

use = Blueprint('use', __name__)


@use.route('/UsersRegistry', methods=['POST', ])
def users_registry():
    username = str(request.form['username']).strip().lower()
    name = str(request.form['name']).strip().title()
    surname = str(request.form['surname']).strip().title()

    session['username'] = username
    session['name'] = name
    session['surname'] = surname

    if UsersRepository().FindByUsername(username):
        flash('Nome de usuário já cadastrado, tente outro', 'info')
        return redirect(url_for('log.nova_conta'))
    else:
        UsersRepository().New(username, name, surname)
        flash("Usuário criado com sucesso. Use a senha 'pass' no primeiro acesso.", 'success')
        CleanLoginItens()
        return redirect(url_for('log.login'))
