import db.db_connect as db
from db.db_helpers import TryDBMessage
from models import Comentations

msdb = db.con()

#   <--- Comentarios DEFs beginning --->

def comentarios_new(resenha_id, user_id, review, date):  # <- Register a new 'Comentario' in the table ->
    try:
        cursor = msdb.cursor()
        insert = f"INSERT INTO public.comentarios (resenha_id, user_id, review, date) " \
                 f"VALUES (%s, %s, %s, %s)"
        cursor.execute(insert, (resenha_id, user_id, review, date))
        msdb.commit()
    except:
        TryDBMessage.message()


def comentarios_list(resenha_id):  # <- List Comentario registered accordingly to the 'Resenha' ID ->
    cursor = msdb.cursor()
    cursor.execute("ROLLBACK")
    cursor.execute(f"SELECT * FROM public.comentarios where resenha_id='{resenha_id}'")
    comment = translate_comentarios(cursor.fetchall())
    return comment


# <--- Comentarios DEFs ending --->

def translate_comentarios(comentario):  # <- Converts DB data (comentario) into Tuple ->
    def create_comentario_with_tuple(tuple):
        return Comentations(tuple[0], tuple[1], tuple[2], tuple[3], tuple[4])

    return list(map(create_comentario_with_tuple, comentario))