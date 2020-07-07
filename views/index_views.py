from flask import render_template, session, redirect, url_for, Blueprint
from jinja2 import Environment

from repository.users_repos import UsersRepository
from repository.resenha_repos import ResenhaRepository

ind = Blueprint('ind', __name__, url_prefix='')


@ind.route('/')
def index():
    __createSessionVariables()
    return redirect(url_for('ind.home'))


@ind.route('/home/')
def home():
    review = ResenhaRepository().List(6)
    users = UsersRepository().List()
    return render_template('index.html', resenhas=review, users=users)


@ind.route('/home/<ordering>/')
def home_ordering(ordering):
    review = ResenhaRepository().List()
    users = UsersRepository().List()

    return render_template('index.html', resenhas=review, users=users, ordering=ordering)

def __createSessionVariables():
    session['id'] = ''
    session['username'] = ''
    session['name'] = ''
    session['surname'] = ''
    session['access_level'] = ''
    session['nome_review'] = ''
    session['nome_banda'] = ''
    session['review'] = ''
