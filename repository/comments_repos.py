from .base_repos import PostgreDB
from models.comentations_model import Comentations


class CommentsRepository:

    # <- Register a new 'Comentario' in the table ->
    def New(self, resenha_id, user_id, review, date):
        db = PostgreDB()
        try:
            insert = f"INSERT INTO public.comentarios (resenha_id, user_id, review, date) VALUES ('{resenha_id}', '{user_id}', '{review}', '{date}')"
            db.query(insert)
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- List Comentario registered accordingly to the 'Resenha' ID ->
    def List(self, resenha_id):
        db = PostgreDB()
        try:
            db.query(f"SELECT * FROM public.comentarios where resenha_id='{resenha_id}'")
            return self.__toList(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Delete a comment on DB ->
    def Delete(self, comment_id):
        db = PostgreDB()
        try:
            db.query(f"DELETE FROM public.comentarios WHERE id='{comment_id}'")
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Delete comments on DB when a review is deleted ->
    def DeleteAllComments(self, resenha_id):
        db = PostgreDB()
        try:
            db.query(f"DELETE FROM public.comentarios WHERE RESENHA_ID='{resenha_id}'")
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # Private Methods
    def __toList(self, item):
        def add(item):
            try:
                return Comentations(item[0], item[1], item[2], item[3], item[4])
            except Exception as exp:
                print(exp)

        try:
            return list(map(add, item))
        except Exception as exp:
            print(exp)
