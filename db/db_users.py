import db.db_connect as db
from db.db_helpers import TryDBMessage
from models import Users

msdb = db.con()


#   <--- Users DEFs beginning --->

def users_new(username, name, surname):  # <- Register a new 'User' in the table ->
    try:
        cursor = msdb.cursor()
        insert = f"INSERT INTO public.users (username, name, surname, password) " \
                 f"VALUES (%s, %s, %s, %s)"
        cursor.execute(insert, (username, name, surname, 'pass'))
        msdb.commit()
    except:
        TryDBMessage.message()


def users_password_update(id, new_password):  # <- Update User's password ->
    try:
        cursor = msdb.cursor()
        print(id, new_password)
        updating_query = f"UPDATE public.users SET PASSWORD='{new_password}' WHERE id='{id}'"
        cursor.execute(updating_query)
        msdb.commit()
    except:
        TryDBMessage.message()


def users_list():  # <- List USERS registered ->
    cursor = msdb.cursor()
    cursor.execute("ROLLBACK")
    cursor.execute(f"SELECT * FROM public.users")
    users = translate_users(cursor.fetchall())
    return users


def users_update(id, new_username, new_register, surname):  # <- Update an existent User ->
    try:
        cursor = msdb.cursor()
        updating_query = f"UPDATE public.users SET USERNAME='{new_username}', NAME='{new_register}', SURNAME='{surname}' WHERE id='{id}'"
        cursor.execute(updating_query)
        msdb.commit()
    except:
        TryDBMessage.message()


def user_find_id(id):  # <- ID finder to redirect to resenhas page ->
    cursor = msdb.cursor()
    cursor.execute("ROLLBACK")
    cursor.execute(f"SELECT * FROM public.users where id = {id}")
    find = cursor.fetchone()
    return Users(find[0], find[1], find[2], find[3], find[4])


# <--- Users DEFs ending --->

def translate_users(user):  # <- Converts DB data (user) into Tuple ->
    def create_user_with_tuple(tuple):
        return Users(tuple[0], tuple[1], tuple[2], tuple[3], tuple[4])

    return list(map(create_user_with_tuple, user))