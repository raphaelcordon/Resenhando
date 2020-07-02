from flask import redirect, request, url_for, flash, Blueprint
from repository.users_repos import UsersRepository

use = Blueprint('use', __name__)

# <--- Users routes beginning --->


@use.route('/UsersRegistry', methods=['POST', ])
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
    return redirect(url_for('adm.usuarios'))
