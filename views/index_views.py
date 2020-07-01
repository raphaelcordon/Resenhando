from flask import render_template, session, redirect, url_for, Blueprint
from repository.users_repos import UsersRepository
from repository.resenha_repos import ResenhaRepository
from views.login_views import *
from views.adm_views import *

ind = Blueprint('ind', __name__, url_prefix='')


@ind.route('/')
def index():
    __createSessionVariables()
    return redirect(url_for('ind.home'))


@ind.route('/home/')
def home():
    review = ResenhaRepository().List()
    users = UsersRepository().List()
    return render_template('index.html', resenhas=review, users=users)


def __createSessionVariables():
    session['id'] = ''
    session['username'] = ''
    session['name'] = ''
    session['access_level'] = ''