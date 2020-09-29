from views.adm_views import adm
from views.comentarios_views import com
from views.curtidas_views import cur
from views.filterReviews_views import filter
from views.index_views import ind
from views.login_views import log
from views.notifications_views import notify
from views.resenha_views import res
from views.users_views import use

from flask import Flask

app = Flask(__name__)
app.jinja_options['extensions'].append('jinja2.ext.do')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


app.register_blueprint(adm)
app.register_blueprint(com)
app.register_blueprint(cur)
app.register_blueprint(filter)
app.register_blueprint(ind)
app.register_blueprint(log)
app.register_blueprint(notify)
app.register_blueprint(res)
app.register_blueprint(use)

if __name__ == '__main__':
    app.run()
