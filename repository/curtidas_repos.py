from .base_repos import PostgreDB
from models.curtidas_model import Curtidas, CurtidasCount


class CurtidasRepository:

    # <- Register 'Likes' in the table ->
    def New(self, user_id, resenha_id):
        db = PostgreDB()
        try:
            insert = f"INSERT INTO public.curtidas_hist (user_id, resenha_id) VALUES (%s, %s)"
            db.queryParams(insert, (user_id, resenha_id))
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Check if the 'Resenha' has a 'Like from the current user in the table ->
    def FindById(self, user_id=None, resenha_id=None):
        db = PostgreDB()
        try:
            db.query(
                f"SELECT * FROM public.curtidas_hist where USER_ID = {user_id} and RESENHA_ID = {resenha_id}")
            return self.__toList(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    def CountLikes(self, resenha_id):
        db = PostgreDB()
        try:
            db.query(
                f"SELECT COUNT(resenha_id) FROM public.curtidas_hist where resenha_id = {resenha_id}")
            return self.__toCount(db.fetchOne())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- List Likes registered accordingly to the 'Author_id' ->
    def listAuthorId(self, authorID):
        db = PostgreDB()
        try:
            db.query(
                f"SELECT * FROM public.curtidas_hist WHERE resenha_id IN (SELECT id FROM public.resenha WHERE"
                f" author_id = { authorID }) AND login_date > current_timestamp - interval '30 day'"
                f" ORDER BY login_date DESC")
            return self.__toList(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Update an User of a like ->
    def LikeNew(self, id):
        db = PostgreDB()
        try:
            db.query(f"UPDATE public.users SET read_like='true' WHERE id = {id}")
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Update an User of like read ->
    def LikeRead(self, id):
        db = PostgreDB()
        try:
            db.query(f"UPDATE public.users SET read_like='false' WHERE id = {id}")
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Delete an user on DB ->
    def Delete(self, user_id, resenha_id):
        db = PostgreDB()
        try:
            db.query(
                f"DELETE FROM public.curtidas_hist where user_id = {user_id} and resenha_id = {resenha_id}")
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # Private Methods
    def __toList(self, item):
        def add(item):
            try:
                return self.__toOne(item)
            except Exception as exp:
                print(exp)

        try:
            return list(map(add, item))
        except Exception as exp:
            print(exp)

    def __toOne(self, item):
        try:
            return Curtidas(item[0], item[1], item[2], item[3])
        except Exception as exp:
            print(exp)

    def __toCount(self, item):
        try:
            return CurtidasCount(item[0])
        except Exception as exp:
            print(exp)
