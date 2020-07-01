from datetime import date
from flask import session, redirect, request, url_for, flash, Blueprint
from repository.comments_repos import CommentsRepository

com = Blueprint('com', __name__)

# <--- 'Comentarios' routes beginning --->

@com.route('/comentario', methods=['GET', 'POST'])
def comentario():
    id_resenha = request.form['id']
    id_user = session['id']
    review = request.form['comentario']
    comment_date = date.today()
    CommentsRepository().New(id_resenha, id_user, review, comment_date)
    id = int(id_resenha)
    return redirect(url_for('res.resenhado', id=id))


@com.route('/CommentDelete/<int:comment_id>/<int:resenha_id>')
def CommentDelete(comment_id, resenha_id):
    CommentsRepository().Delete(comment_id)
    flash('Comment Successfully removed', 'info')
    return redirect(url_for('res.resenhado', id=resenha_id))

