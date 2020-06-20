import psycopg2
from models import Users, Resenha

msdb = psycopg2.connect(
    host='ec2-54-75-246-118.eu-west-1.compute.amazonaws.com',
    database='d89gkq7l8caqks',
    user='xcdauuhtrmsrhw',
    port='5432',
    password='b6e8f984b04f80bf4311d33f68a2e6c04ce062540161e7f092c3b047c4cca9e5',
)


#   <--- Authentication DEFs beginning --->

def authenticate(username):
    try:
        cursor = msdb.cursor()
        cursor.execute("ROLLBACK")
        cursor.execute(f"SELECT * FROM public.users where username = '{username}'")
        find = cursor.fetchone()
        return Users(find[0], find[1], find[2], find[3], find[4])
    except:
        TryDBMessage.message()


# <--- Authentication DEFs Ending --->


#   <--- Resenhas DEFs beginning --->

def resenha_list():  # <- List Courses on Courses Page ->
    cursor = msdb.cursor()
    cursor.execute("ROLLBACK")
    cursor.execute(f"SELECT * FROM public.course")
    resenha = translate_resenha(cursor.fetchall())
    return resenha


def resenha_new(tipo_review, author_id, spotify_link, nome_review,
                nome_banda, review, date_register, image_file=None):  # <- Register a new 'Resenha' in the table ->
    try:
        cursor = msdb.cursor()
        cursor.execute = f"INSERT INTO public.resenha (tipo_review, author_id, spotify_link, nome_review, " \
                         f"nome_banda, review, date_register, image_file) " \
                         f"VALUES ('{tipo_review}', '{author_id}', '{spotify_link}', '{nome_review}', " \
                         f"'{nome_banda}', '{review}', '{date_register}', '{image_file}')"
        msdb.commit()
    except:
        TryDBMessage.message()


# <--- Resenhas DEFs ending --->


#   <--- Users DEFs beginning --->

def users_new(username, name, surname, password):  # <- Register a new 'User' in the table ->
    try:
        cursor = msdb.cursor()
        cursor.execute = f"INSERT INTO public.users (username, name, surname, password) " \
                         f"VALUES ('{username}', '{name}', '{surname}', '{password}')"
        msdb.commit()
    except:
        TryDBMessage.message()


# <--- Users DEFs ending --->


#   <--- Translating DB beginning --->
def translate_resenha(resenha):  # <- Converts DB data (resenha) into Tuple ->
    def create_resenha_with_tuple(tuple):
        return Resenha(tuple[0], tuple[1], tuple[2], tuple[3], tuple[4], tuple[5], tuple[6], tuple[7], tuple[8])

    return list(map(create_resenha_with_tuple, resenha))


def translate_users(user):  # <- Converts DB data (resenha) into Tuple ->
    def create_user_with_tuple(tuple):
        return Users(tuple[0], tuple[1], tuple[2], tuple[3], tuple[4])

    return list(map(create_user_with_tuple, user))


# <--- Translating DB ending --->


class TryDBMessage:
    @staticmethod
    def message():  # <- Raise an error on the log if the table isn't found ->
        return f'The connection with the database filed.\n' \
               f" Make sure you have executed the script 'db_script.sql' in MySQL."
