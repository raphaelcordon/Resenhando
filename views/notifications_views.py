from flask import session, redirect, url_for, flash, Blueprint, render_template
from repository.comments_repos import CommentsRepository
from repository.users_repos import UsersRepository
from repository.curtidas_repos import CurtidasRepository
from repository.resenha_repos import ResenhaRepository


notify = Blueprint('notify', __name__)


@notify.route('/notifications', methods=['GET', 'POST'])
def notifications():
    if session['email'] == '' or 'email' not in session:
        flash('Você precisa logar para acessar essa área', 'info')
        return redirect(url_for('ind.home'))
    else:
        comments = CommentsRepository().listAuthorId(session['id'])
        likeNotifications = CurtidasRepository().listAuthorId(session['id'])
        usersNotifications = UsersRepository().List()
        resenhasListAll = ResenhaRepository().ListAll()
        notifyComment = UsersRepository().FindById(session['id']).read_comment
        notifyLike = UsersRepository().FindById(session['id']).read_like

        return render_template('partials/modalNotifications.html', comments=comments,
                           usersNotifications=usersNotifications, likeNotifications=likeNotifications,
                               resenhasListAll=resenhasListAll, notifyComment=notifyComment, notifyLike=notifyLike)
