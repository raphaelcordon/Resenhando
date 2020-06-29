import db.db_connect as db
from db.db_helpers import TryDBMessage
from models import Resenha

msdb = db.con()

#   <--- Resenhas DEFs beginning --->

def resenha_list():
    """
    List Reviews on Index Page
    :return: Everything from Table public.resenha
    """
    cursor = msdb.cursor()
    cursor.execute("ROLLBACK")
    cursor.execute(f"SELECT * FROM public.resenha")
    resenha = translate_resenha(cursor.fetchall())
    return resenha


def resenha_new(tipo_review, author_id, spotify_link, nome_review,
                nome_banda, review, date_register, image_file):  # <- Register a new 'Resenha' in the table ->
    try:
        cursor = msdb.cursor()
        insert = f"INSERT INTO public.resenha (tipo_review, author_id, spotify_link, nome_review, " \
                         f"nome_banda, review, date_register, image_file) " \
                 f"VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert, (tipo_review, author_id, spotify_link, nome_review,
                nome_banda, review, date_register, image_file))
        msdb.commit()
    except:
        TryDBMessage.message()


def resenha_find_id(id):  # <- ID finder to redirect to Edit page ->
    cursor = msdb.cursor()
    cursor.execute(f"SELECT * FROM public.resenha where id = {id}")
    find = cursor.fetchone()
    return Resenha(find[0], find[1], find[2], find[3], find[4], find[5], find[6], find[7], find[8])


def resenha_author_id(id):  # <- ID finder to redirect to Edit page ->
    cursor = msdb.cursor()
    cursor.execute(f"SELECT * FROM public.resenha where author_id = {id}")
    resenha = translate_resenha(cursor.fetchall())
    return resenha


def resenha_find_capa(id):  # <- ID finder to redirect to Edit page ->
    cursor = msdb.cursor()
    cursor.execute(f"SELECT image_file FROM public.resenha where id = {id}")
    capa = cursor.fetchall()
    return capa


def resenha_edit(id, tipo_review, spotify_link, nome_review,
                nome_banda, review, date_register, image_file):  # <- Register a new 'Resenha' in the table ->
    try:
        cursor = msdb.cursor()
        cursor.execute("ROLLBACK")
        updating_query = f"update public.resenha set tipo_review='{tipo_review}', spotify_link='{spotify_link}', " \
                         f"nome_review='{nome_review}', nome_banda='{nome_banda}', review='{review}', " \
                         f"date_register='{date_register}', image_file='{image_file}' where id='{id}'"
        cursor.execute(updating_query)
        msdb.commit()
    except:
        TryDBMessage.message()


def translate_resenha(resenha):
    """
    Converts DB data (resenha) into Tuple
    :param resenha: comes from def resenha_list
    :return: Tuple with data from Table public.resenha
    """
    def create_resenha_with_tuple(tuple):
        return Resenha(tuple[0], tuple[1], tuple[2], tuple[3], tuple[4], tuple[5], tuple[6], tuple[7], tuple[8])

    return list(map(create_resenha_with_tuple, resenha))