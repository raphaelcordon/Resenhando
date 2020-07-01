import os
from datetime import date
from passlib.hash import sha256_crypt
from flask import Flask, render_template, session, redirect, request, url_for, flash, send_from_directory
from repository.users_repos import UsersRepository
from repository.resenha_repos import ResenhaRepository
from repository.comments_repos import CommentsRepository
from repository.auth_repos import AuthenticateRepository
from models.users_model import UsersPass
from models.common import DateConversion
from thirdparty.spotify import SpotifyLink, SpotifyImage, SpotifyTipoResenha

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


def __createSessionVariables():
    session['id'] = ''
    session['username'] = ''
    session['name'] = ''
    session['access_level'] = ''


@app.route('/')
def index():
    __createSessionVariables()
    return redirect(url_for('home'))


@app.route('/home/')
def home():
    review = ResenhaRepository().List()
    users = UsersRepository().List()
    return render_template('index.html', resenhas=review, users=users)


# <--- 'Resenha' routes beginning --->

@app.route('/resenha', methods=['GET', 'POST'])
def resenha():
    if session['username'] == '' or 'username' not in session:
        flash('Você precisa logar para acessar essa área', 'danger')
        return redirect(url_for('index'))

    flash('!!!IMPORTANTE!!! Sem um link do Spotify, sua resenha NÃO irá ao ar.', 'warning')
    return render_template('resenha.html')


@app.route('/nova_resenha', methods=['GET', 'POST'])
def nova_resenha():
    if session['username'] == '' or 'username' not in session:
        flash('Você precisa logar para acessar essa área', 'danger')
        return redirect(url_for('index'))

    tipo_review = str(SpotifyTipoResenha(str(request.form['spotify_link'])))
    author_id = session['id']
    spotify_link = str(SpotifyLink(str(request.form['spotify_link'])))

    if '' == spotify_link:
        flash('Link do Spotify invalido', 'danger')
        return render_template('resenha.html')

    nome_review = request.form['nome_review']
    nome_banda = request.form['nome_banda']
    review = request.form['review']
    date_register = date.today()
    filename = str(SpotifyImage(str(request.form['spotify_link'])))

    ResenhaRepository().New(tipo_review, author_id, spotify_link,
                            nome_review, nome_banda, review, date_register, filename)

    return redirect(url_for('home'))


@app.route('/editar_resenha/<int:id>', methods=['GET', 'POST'])
def editar_resenha(id):
    resenha = ResenhaRepository().FindById(id)
    flash('!!!IMPORTANTE!!!   Sem um link do Spotify, sua resenha NÃO irá ao ar.', 'warning')
    return render_template('editar_resenha.html', resenha=resenha)


@app.route('/atualizar_resenha', methods=['GET', 'POST'])
def atualizar_resenha():
    id = request.form['id']
    tipo_review = str(SpotifyTipoResenha(str(request.form['spotify_link'])))
    spotify_link = str(SpotifyLink(str(request.form['spotify_link'])))

    if '' == spotify_link:
        resenha = ResenhaRepository().FindById(id)
        flash('Link do Spotify inválido', 'danger')
        return render_template('editar_resenha.html', resenha=resenha)

    nome_review = request.form['nome_review']
    nome_banda = request.form['nome_banda']
    review = request.form['review']
    date_register = date.today()
    filename = str(SpotifyImage(str(request.form['spotify_link'])))

    ResenhaRepository().Edit(id, tipo_review, spotify_link, nome_review,
                             nome_banda, review, date_register, filename)
    flash('Resenha atualizada com sucesso', 'success')
    return redirect(url_for('minhas_resenhas', id=session['id']))


@app.route('/resenhado/<int:id>/')
def resenhado(id):
    data = ResenhaRepository().FindById(id)
    user_author = UsersRepository().FindById(data.author_id)
    date = DateConversion(str(data.date_register))

    comments = CommentsRepository().List(id)
    comment_user = UsersRepository().List()

    return render_template('resenhado.html', data=data, user_author=user_author,
                           date=date, comments=comments, comment_user=comment_user)


@app.route('/home/<int:id>/')
def minhas_resenhas(id):
    if session['username'] == '' or 'username' not in session:
        flash('Você precisa logar para acessar essa área', 'danger')
        return redirect(url_for('home'))

    resenhas = ResenhaRepository().FindAuthorById(id)
    flash('Essas são as resenhas criadas por você até o momento', 'info')
    return render_template('index.html', resenhas=resenhas)


@app.route('/static/img/bg-img/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('static/img/bg-img/', nome_arquivo)


def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo
        else:
            return 'No-Image-Available.png'


@app.route('/image/<file_name>')
def image(file_name):
    return send_from_directory('image', file_name)

# <--- 'Comentarios' routes beginning --->


@app.route('/comentario', methods=['GET', 'POST'])
def comentario():
    id_resenha = request.form['id']
    id_user = session['id']
    review = request.form['comentario']
    comment_date = date.today()
    CommentsRepository().New(id_resenha, id_user, review, comment_date)
    id = int(id_resenha)
    return redirect(url_for('resenhado', id=id))


@app.route('/CommentDelete/<int:comment_id>/<int:resenha_id>')
def CommentDelete(comment_id, resenha_id):
    CommentsRepository().Delete(comment_id)
    flash('Comment Successfully removed', 'info')
    return redirect(url_for('resenhado', id=resenha_id))

# <--- Login/Logout and Change Pass routes beginning --->


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/authenticate', methods=['POST', ])
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
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    __createSessionVariables()
    return redirect(url_for('home'))


@app.route('/change_pass')
def change_pass():
    id = session['id']
    return render_template('change_pass.html', data=id)


@app.route('/update_pass_db', methods=['POST', ])
def update_pass_db():
    id = session['id']
    password = sha256_crypt.hash(str(request.form['password']))
    new_pass = UsersPass(id, password)
    UsersRepository().UpdatePassword(new_pass.id, new_pass.password)
    flash('Senha alterada com sucesso', 'success')
    return redirect(url_for('home'))

# <--- Users routes beginning --->


@app.route('/UsersRegistry', methods=['POST', ])
def users_registry():
    username = str(request.form['username']).strip().lower()
    name = str(request.form['name']).strip().title()
    surname = str(request.form['surname']).strip().title()

    if username == '' or name == '' or surname == '':
        flash('Blank field not accepted', 'info')
    elif UsersRepository().New(username, name, surname):
        flash('Already registered, please check below', 'info')
    else:
        flash("Successfully created. User the password 'pass' to login for the first time.", 'success')
    return redirect(url_for('usuarios'))

# <--- ADMINISTRATIVE routes beginning --->


@app.route('/usuarios')
def usuarios():
    users_list = UsersRepository().List()
    return render_template('_usuarios.html', users=users_list)


@app.route('/UsuariosDelete/<int:user_id>')
def UsuariosDelete(user_id):
    UsersRepository().Delete(user_id)
    flash('Usuario Successfully removed', 'info')
    return redirect(url_for('usuarios'))


@app.route('/adm_resenhas')
def adm_resenhas():
    resenhas = ResenhaRepository().List()
    return render_template('_adm_resenhas.html', resenhas=resenhas)


@app.route('/ResenhasDelete/<int:resenha_id>')
def ResenhasDelete(resenha_id):
    ResenhaRepository().Delete(resenha_id)
    flash('Resenha Successfully removed', 'info')
    return redirect(url_for('adm_resenhas'))


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


if __name__ == '__main__':
    app.run()
