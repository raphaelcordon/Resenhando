from passlib.hash import sha256_crypt
from flask import render_template, session, redirect, request, url_for, flash, Blueprint
from repository.users_repos import UsersRepository
from repository.auth_repos import AuthenticateRepository
from repository.login_hist_repos import LoginHistRepository
from models.users_model import UsersPass

log = Blueprint('log', __name__)


@log.route('/login')
def login():
    previous = session['previous']
    return render_template('login.html', previous=previous)


@log.route('/authenticate', methods=['POST', ])
def authenticate():
    # <- Check Username ->
    session['username'] = request.form['username']
    if AuthenticateRepository().auth(
            str(request.form['username']).lower().strip()):
        user = AuthenticateRepository().auth(
            str(request.form['username']).lower().strip())
    else:
        flash('Verifique usuário e/ou senha e tente novamente', 'danger')
        return redirect(url_for('log.login'))

    # <- Check Password ->
    if user.password == 'pass':
        UpdateSession(user)
        LoginHistRepository().New(str(session['id']))  # input Timestamp in db
        return redirect(url_for('log.change_pass'))
    elif sha256_crypt.verify(request.form['password'], user.password):
        UpdateSession(user)
        LoginHistRepository().New(str(session['id']))  # input Timestamp in db
        flash(f'Bem vindo {user.name}', 'success')
        if request.form['previous'] != 'None' or request.form['previous'] != '':
            return redirect(url_for(request.form['previous']))
        else:
            return redirect(url_for('ind.home'))
    else:
        flash('Verifique usuário e/ou senha e tente novamente', 'danger')
        return redirect(url_for('log.login'))


@log.route('/logout')
def logout():
    """
    :return: Cleaning Session
    """
    previous = request.headers.get("Referer")
    session['id'] = ''
    session['username'] = ''
    session['name'] = ''
    session['surname'] = ''
    session['access_level'] = ''
    session['nome_review'] = ''
    session['nome_banda'] = ''
    session['review'] = ''

    return redirect(previous)


@log.route('/nova_conta')
def nova_conta():
    return render_template('nova_conta.html')


#  <---- defs related to PASSWORD beginning ---->

@log.route('/change_pass')
def change_pass():
    id = session['id']
    return render_template('change_pass.html', data=id)


@log.route('/update_pass_db', methods=['POST', ])
def update_pass_db():
    id = session['id']
    if request.form['password'] == request.form['password2']:
        password = sha256_crypt.hash(str(request.form['password']))
        new_pass = UsersPass(id, password)
        UsersRepository().UpdatePassword(new_pass.id, new_pass.password)
        flash('Senha alterada com sucesso', 'success')
        return redirect(url_for('ind.home'))
    else:
        flash('As senhas não são identicas, tente novamente', 'danger')
        return redirect(url_for('log.change_pass'))


#  <-- Reset Pass -->

@log.route('/reset_pass')
def reset_pass():
    return render_template('reset_pass.html')


@log.route('/reset_pass_db', methods=['POST', ])
def reset_pass_db():
    if not UsersRepository().FindByUsername(request.form['username']):
        flash('Nome de usuário não encontrado', 'info')
        return redirect(url_for('log.reset_pass'))
    else:
        UsersRepository().ResetPassword(str(request.form['username']))
        flash("Senha resetada para 'pass' ", 'success')
        return redirect(url_for('log.login'))


#  <---- defs related to PASSWORD ending ---->


def UpdateSession(user):
    """
    :param user: list info from user from db
    :return: Session populated with current user's info
    id / username / name / surname / password (encripted) or initial ('pass')
    """
    session['id'] = user.id
    session['username'] = user.username
    session['name'] = user.name
    session['surname'] = user.surname
    session['password'] = user.password


