from passlib.hash import sha256_crypt
from flask import render_template, session, redirect, request, url_for, flash, Blueprint
from repository.users_repos import UsersRepository
from repository.auth_repos import AuthenticateRepository
from models.users_model import UsersPass

log = Blueprint('log', __name__)

# <--- Login/Logout and Change Pass routes beginning --->


@log.route('/login')
def login():
    return render_template('login.html')


@log.route('/authenticate', methods=['POST', ])
def authenticate():
    try:
        user = AuthenticateRepository().auth(
            str(request.form['username']).lower().strip())
        try:
            check_pass = sha256_crypt.verify(
                request.form['password'], user.password)
        except:
            check_pass = request.form['password'], user.password
        finally:
            session['id'] = user.id
            session['username'] = user.username
            session['name'] = user.name
            session['surname'] = user.surname
            session['password'] = user.password

        if user.password == 'pass':
            return redirect(url_for('change_pass'))
        elif not sha256_crypt.verify(request.form['password'], user.password):
            flash('Login falhou, por favor tente novamente', 'danger')
            return redirect(url_for('login'))
        else:
            if check_pass:
                flash(f'Bem vindo {user.name}', 'success')
                return redirect(url_for('home'))
            else:
                flash('Login falhou, por favor tente novamente', 'danger')
                return redirect(url_for('login'))
    except:
        flash('Verifique username e/ou senha e tente novamente', 'danger')
        return redirect(url_for('log.login'))


@log.route('/logout')
def logout():
    session['id'] = ''
    session['username'] = ''
    session['name'] = ''
    session['access_level'] = ''
    return redirect(url_for('ind.home'))


@log.route('/change_pass')
def change_pass():
    id = session['id']
    return render_template('change_pass.html', data=id)


@log.route('/update_pass_db', methods=['POST', ])
def update_pass_db():
    id = session['id']
    password = sha256_crypt.hash(str(request.form['password']))
    new_pass = UsersPass(id, password)
    UsersRepository().UpdatePassword(new_pass.id, new_pass.password)
    flash('Senha alterada com sucesso', 'success')
    return redirect(url_for('ind.home'))