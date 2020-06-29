from flask import Flask, render_template, session, redirect, request, url_for, flash, send_from_directory
import db
import os
from models import EditUsersPass, DateConversion
from spotify import SpotifyLink, SpotifyImage, SpotifyTipoResenha
from passlib.hash import sha256_crypt
from datetime import date
from time import time

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    logout()
    return redirect('home')


@app.route('/home/')
def home():
    resenhas = db.resenha_list()
    users = db.users_list()
    return render_template('index.html', resenhas=resenhas, users=users)


# <--- 'Resenha' routes beginning --->

@app.route('/resenha', methods=['GET', 'POST'])
def resenha():
    if session['username'] == '' or 'username' not in session:
        flash('Você precisa logar para acessar essa área', 'danger')
        return redirect(url_for('index'))
    else:
        flash('!!!IMPORTANTE!!!   Sem um link do Spotify, sua resenha NÃO irá ao ar.', 'warning')
        return render_template('resenha.html')


@app.route('/nova_resenha', methods=['GET', 'POST'])
def nova_resenha():
    if session['username'] == '' or 'username' not in session:
        flash('Você precisa logar para acessar essa área', 'danger')
        return redirect(url_for('index'))
    else:
        tipo_review = str(SpotifyTipoResenha(str(request.form['spotify_link'])))
        author_id = session['id']
        spotify_link = str(SpotifyLink(str(request.form['spotify_link'])))
        nome_review = request.form['nome_review']
        nome_banda = request.form['nome_banda']
        review = request.form['review']
        date_register = date.today()
        filename = str(SpotifyImage(str(request.form['spotify_link'])))

        db.resenha_new(tipo_review, author_id, spotify_link, nome_review, nome_banda, review, date_register, filename)

        return redirect(url_for('home'))


@app.route('/editar_resenha/<int:id>', methods=['GET', 'POST'])
def editar_resenha(id):
    resenha = db.resenha_find_id(id)
    flash('!!!IMPORTANTE!!!   Sem um link do Spotify, sua resenha NÃO irá ao ar.', 'warning')
    return render_template('editar_resenha.html', resenha=resenha)


@app.route('/atualizar_resenha', methods=['GET', 'POST'])
def atualizar_resenha():

    id = request.form['id']
    tipo_review = str(SpotifyTipoResenha(str(request.form['spotify_link'])))
    spotify_link = str(SpotifyLink(str(request.form['spotify_link'])))
    nome_review = request.form['nome_review']
    nome_banda = request.form['nome_banda']
    review = request.form['review']
    date_register = date.today()
    filename = str(SpotifyImage(str(request.form['spotify_link'])))

    db.resenha_edit(id, tipo_review, spotify_link, nome_review, nome_banda, review, date_register, filename)

    flash('Resenha atualizada com sucesso', 'success')
    return redirect(url_for('minhas_resenhas', id=session['id']))


@app.route('/resenhado/<int:id>/')
def resenhado(id):
    data = db.resenha_find_id(id)
    user_author = db.user_find_id(data.author_id)
    date = DateConversion(str(data.date_register))

    comments = db.comentarios_list(id)
    comment_user = db.users_list()
    for c in comments:
        print(c.comment_date)
    return render_template('resenhado.html', data=data, user_author=user_author, date=date,
                           comments=comments, comment_user=comment_user)


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


@app.route('/home/<int:id>/')
def minhas_resenhas(id):
    if session['username'] == '' or 'username' not in session:
        flash('Você precisa logar para acessar essa área', 'danger')
        return redirect(url_for('home'))
    else:
        resenhas = db.resenha_author_id(id)
        flash('Essas são as resenhas criadas por você até o momento', 'info')
        return render_template('index.html', resenhas=resenhas)


# <--- 'Resenha' routes ending --->

# <--- 'Comentarios' routes beginning --->

@app.route('/comentario', methods=['GET', 'POST'])
def comentario():
    id_resenha = request.form['id']
    id_user = session['id']
    review = request.form['comentario']
    comment_date = date.today()
    db.comentarios_new(id_resenha, id_user, review, comment_date)
    id = int(id_resenha)
    return redirect(url_for('resenhado', id=id))



# <--- 'Comentarios' routes ending --->


# <--- Login/Logout and Change Pass routes beginning --->


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/authenticate', methods=['POST',])
def authenticate():
    try:
        user = db.authenticate(str(request.form['username']).lower().strip())
        try:
            check_pass = sha256_crypt.verify(request.form['password'], user.password)
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
    session['id'] = ''
    session['username'] = ''
    session['name'] = ''
    session['access_level'] = ''
    return redirect(url_for('home'))


@app.route('/change_pass')
def change_pass():
    id = session['id']
    return render_template('change_pass.html', data=id)


@app.route('/update_pass_db', methods=['POST',])
def update_pass_db():
    id = session['id']
    password = sha256_crypt.hash(str(request.form['password']))
    new_pass = EditUsersPass(id, password)
    db.users_password_update(new_pass.id, new_pass.password)
    flash('Senha alterada com sucesso', 'success')
    return redirect(url_for('home'))


# <--- Login/Logout routes ending --->


# <--- Users routes beginning --->

@app.route('/UsersRegistry', methods=['POST',])
def users_registry():
    username = str(request.form['username']).strip().lower()
    name = str(request.form['name']).strip().title()
    surname = str(request.form['surname']).strip().title()

    if username == '' or name == '' or surname == '':
        flash('Blank field not accepted', 'info')
    elif db.users_new(username, name, surname):
        flash('Already registered, please check below', 'info')
    else:
        flash("Successfully created. User the password 'pass' to login for the first time.", 'success')
    return redirect(url_for('usuarios'))


@app.route('/Delete/<string:table>/<int:id>/')
def Delete(table, id):
    db.DeletingDB(table, id)
    flash('Successfully removed', 'info')
    if table == 'users':
        return redirect(url_for('usuarios'))
    elif table == 'resenha':
        try:
            capa = db.resenha_find_capa(request.form['id'])
            capa = capa[0][0]
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], capa))
        except:
            pass
        return redirect(url_for('adm_resenhas'))
    else:
        return redirect(url_for('home'))


# <--- ADMINISTRATIVE routes beginning --->

@app.route('/usuarios')
def usuarios():
    users_list = db.users_list()
    return render_template('_usuarios.html', users=users_list)


@app.route('/adm_resenhas')
def adm_resenhas():
    resenhas = db.resenha_list()
    return render_template('_adm_resenhas.html', resenhas=resenhas)


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# <--- ADMINISTRATIVE routes ending --->

if __name__ == '__main__':
    app.run(debug=True)
