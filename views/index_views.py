from flask import render_template, session, redirect, url_for, Blueprint
from repository.users_repos import UsersRepository
from repository.resenha_repos import ResenhaRepository
from models.common import CleanSession

ind = Blueprint('ind', __name__, url_prefix='')


@ind.route('/')
def index():
    __createSessionVariables()
    return redirect(url_for('ind.home'))


@ind.route('/home/')
def home():
    CleanSession()
    review = ResenhaRepository().List()
    users = UsersRepository().List()
    return render_template('index.html', resenhas=review, users=users)


def __createSessionVariables():
    session['id'] = ''
    session['username'] = ''
    session['name'] = ''
    session['access_level'] = ''
    session['nome_review'] = ''
    session['nome_banda'] = ''
    session['review'] = ''
