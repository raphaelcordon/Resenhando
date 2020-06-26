from flask import Flask, render_template, session, redirect, request, url_for, flash, send_from_directory
import db
import os
from models import EditUsersPass, DateConversion
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
        flash('Você precisa logar para acessar essa área')
        return redirect(url_for('index'))
    else:
     return render_template('resenha.html')


@app.route('/nova_resenha', methods=['GET', 'POST'])
def nova_resenha():
    if session['username'] == '' or 'username' not in session:
        flash('Você precisa logar para acessar essa área')
        return redirect(url_for('index'))
    else:
        tipo_review = request.form['tipo_review']
        author_id = session['id']
        spotify_link = request.form['spotify_link']
        nome_review = request.form['nome_review']
        nome_banda = request.form['nome_banda']
        review = request.form['review']
        date_register = date.today()


    #   <-- input image -->
        if request.files['image_file']:
            image_file = request.files['image_file']
            ext_file = str(request.files['image_file'])
            if ext_file.lower().endswith('jpg'):
                ext = '.jpg'
            elif ext_file.lower().endswith('jpeg'):
                ext = '.jpeg'
            else:
                ext = '.png'
            timestamp = time()
            filename = f'capa-{timestamp}{ext}'
            image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            filename = None

        db.resenha_new(tipo_review, author_id, spotify_link, nome_review, nome_banda, review, date_register, filename)

        return redirect(url_for('home'))


@app.route('/editar_resenha/<int:id>', methods=['GET', 'POST'])
def editar_resenha(id):
    resenha = db.resenha_find_id(id)
    return render_template('editar_resenha.html', resenha=resenha)


@app.route('/atualizar_resenha', methods=['GET', 'POST'])
def atualizar_resenha():

    id = request.form['id']
    tipo_review = request.form['tipo_review']
    spotify_link = request.form['spotify_link']
    nome_review = request.form['nome_review']
    nome_banda = request.form['nome_banda']
    review = request.form['review']
    date_register = date.today()



    #   <-- input image -->
    if request.files['image_file'].filename == '':
        db.resenha_edit_ni(id, tipo_review, spotify_link, nome_review, nome_banda, review, date_register)
    else:
        capa = db.resenha_find_capa(request.form['id'])
        capa = capa[0][0]
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], capa))
        image_file = request.files['image_file']
        ext_file = str(request.files['image_file'])
        if ext_file.lower().endswith('jpg'):
            ext = '.jpg'
        elif ext_file.lower().endswith('jpeg'):
            ext = '.jpeg'
        else:
            ext = '.png'
        timestamp = time()
        filename = f'capa-{timestamp}{ext}'
        image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        db.resenha_edit_i(id, tipo_review, spotify_link, nome_review, nome_banda, review, date_register, filename)

    return redirect(url_for('minhas_resenhas', id=session['id']))


@app.route('/resenhado/<int:id>/')
def resenhado(id):
    if session['username'] == '' or 'username' not in session:
        flash('Você precisa logar para acessar essa área')
        return redirect(url_for('index'))
    else:
        data = db.resenha_find_id(id)
        user = db.user_find_id(data.author_id)
        date = DateConversion(str(data.date_register))

        return render_template('resenhado.html', data=data, user=user, date=date)


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
        flash('Você precisa logar para acessar essa área')
        return redirect(url_for('home'))
    else:
        resenhas = db.resenha_author_id(id)
        return render_template('index.html', resenhas=resenhas)


# <--- 'Resenha' routes beginning --->


# <--- Login/Logout and Change Pass routes beginning --->


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/authenticate', methods=['POST',])
def authenticate():
    user = db.authenticate(request.form['username'])
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
        flash('Login falhou, por favor tente novamente', 'error')
        return redirect(url_for('login'))
    else:
        if check_pass:
            flash(f'Bem vindo {user.name}')
            return redirect(url_for('home'))
        else:
            flash('Login falhou, por favor tente novamente', 'error')
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
    flash('Senha alterada com sucesso')
    return redirect(url_for('home'))


# <--- Login/Logout routes ending --->


# <--- Users routes beginning --->

@app.route('/UsersRegistry', methods=['POST',])
def users_registry():
    username = str(request.form['username']).strip().lower()
    name = str(request.form['name']).strip().title()
    surname = str(request.form['surname']).strip().title()

    if username == '' or name == '' or surname == '':
        flash('Blank field not accepted')
    elif db.users_new(username, name, surname):
        flash('Already registered, please check below')
    else:
        flash("Successfully created. User the password 'pass' to login for the first time.")
    return redirect(url_for('usuarios'))


@app.route('/Delete/<string:table>/<int:id>/')
def Delete(table, id):
    db.DeletingDB(table, id)
    flash('Successfully removed')
    if table == 'users':
        return redirect(url_for('usuarios'))
    elif table == 'resenha':
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
    app.run()
