from flask import Flask


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

from views.adm_views import adm
from views.comentarios_views import com
from views.index_views import ind
from views.login_views import log
from views.resenha_views import res
from views.users_views import use

app.register_blueprint(adm)
app.register_blueprint(com)
app.register_blueprint(ind)
app.register_blueprint(log)
app.register_blueprint(res)
app.register_blueprint(use)


if __name__ == '__main__':
    app.run(debug=True)
