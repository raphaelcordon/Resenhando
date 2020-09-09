from flask import session, redirect, request, url_for, flash, Blueprint
from repository.comments_repos import CommentsRepository
from repository.resenha_repos import ResenhaRepository

com = Blueprint('com', __name__)


@com.route('/comentario', methods=['GET', 'POST'])
def comentario():
    id_resenha = request.form['id']
    id_user = session['id']
    review = request.form['comentario']
    CommentsRepository().New(id_resenha, id_user, review)
    authorID = ResenhaRepository().FindById(id_resenha).author_id
    CommentsRepository().CommentNew(authorID)
    id = int(id_resenha)
    return redirect(url_for('res.resenhado', id=id))


@com.route('/CommentDelete/<int:comment_id>/<int:resenha_id>')
def CommentDelete(comment_id, resenha_id):
    CommentsRepository().Delete(comment_id)
    flash('Comentário removido com sucesso', 'info')
    return redirect(url_for('res.resenhado', id=resenha_id))


@com.route('/commentRead/')
def commentRead():
    CommentsRepository().CommentRead(session['id'])
