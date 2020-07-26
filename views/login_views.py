from passlib.hash import sha256_crypt
from flask import render_template, session, redirect, request, url_for, flash, Blueprint
from repository.auth_repos import AuthenticateRepository
from repository.login_hist_repos import LoginHistRepository


log = Blueprint('log', __name__)


@log.route('/login')
def login():
    session['previous'] = request.headers.get("Referer")
    if session['previous'] == '':
        previous = 'ind.home'
        session['previous'] = 'ind.home'
    else:
        previous = session['previous']
    return render_template('account/login.html', previous=previous)


@log.route('/authenticate', methods=['POST', 'GET'])
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
    password = request.form['password']
    isValidPass = sha256_crypt.verify(password, user.password)

    print(isValidPass)

    if isValidPass == True:
        if user.changepass:
            return redirect(url_for('use.changePass'))
        else:
            UpdateSession(user)
            # input Timestamp in db
            LoginHistRepository().New(str(session['id']))
            flash(f'Bem vindo {user.name}', 'success')
        
        _redirect = request.form['previous']
        if _redirect != '':
            return redirect(_redirect)
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
    session['id'] = ''
    session['username'] = ''
    session['name'] = ''
    session['surname'] = ''
    session['access_level'] = ''
    session['nome_review'] = ''
    session['nome_banda'] = ''
    session['review'] = ''
    session['previous'] = ''

    return redirect(url_for('ind.home'))


@log.route('/newAccount')
def newAccount():
    return render_template('account/newAccount.html')


def UpdateSession(user):
    """
    :param user: list info from user from db
    :return: Session populated with current user's info
    id / username / name / surname / password (encripted)
    """
    session['id'] = user.id
    session['username'] = user.username
    session['name'] = user.name
    session['surname'] = user.surname
    session['password'] = user.password
