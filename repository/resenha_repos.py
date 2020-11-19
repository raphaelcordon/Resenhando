from .base_repos import PostgreDB
from models.resenha_model import Resenha, ResenhaAuthorId


class ResenhaRepository:

    def List(self, tipo_review='', top=0):
        db = PostgreDB()
        try:
            if top > 0:
                if tipo_review != '':
                    db.query(f"SELECT * FROM public.resenha where tipo_review = '{tipo_review}' "
                             f"order by date_register desc limit {top}")
            else:
                db.query(f"SELECT * FROM public.resenha where tipo_review = '{tipo_review}' "
                         f"order by date_register")
            return self.__toList(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    def ListAll(self):
        db = PostgreDB()
        try:
            db.query(f"SELECT * FROM public.resenha")
            return self.__toList(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    def ListGenres(self, top=0):
        db = PostgreDB()
        try:
            if top > 0:
                db.query(f"SELECT * FROM public.resenha where genre is not Null"
                         f"order by date_register desc limit {top}")
            else:
                db.query(f"SELECT * FROM public.resenha where genre is not Null"
                         f"order by date_register")
            return self.__toList(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    def ListOneGenre(self, tipo_review, genre):
        db = PostgreDB()
        try:
            db.query(f"SELECT * FROM public.resenha where tipo_review = '{tipo_review}' and genre = '{genre}' "
                     f"order by date_register")
            return self.__toList(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Register a new 'Resenha' in the table ->
    def New(self, tipo_review, author_id, nome_review, spotify_id, review, genre):
        db = PostgreDB()
        try:
            insert = f"INSERT INTO public.resenha (tipo_review, author_id, nome_review, spotify_id, review, genre) " \
                f"VALUES (%s, %s, %s, %s, %s, %s)"
            db.queryParams(insert, (tipo_review, author_id,
                                    nome_review, spotify_id, review, genre))
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- ID finder to redirect to Edit page ->
    def FindById(self, id):
        db = PostgreDB()
        try:
            db.query(f"SELECT * FROM public.resenha where id = {id}")
            return self.__toOne(db.fetchOne())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    def FindAuthorByNameSurname(self, name, surname):
        db = PostgreDB()
        try:
            db.query(f"SELECT id FROM public.users where name = '{name}' and surname = '{surname}'")
            return self.__toOneID(db.fetchOne())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- ID finder to redirect to Edit page ->
    def FindAuthorById(self, id):
        db = PostgreDB()
        try:
            db.query(f"SELECT * FROM public.resenha where author_id = {id}")
            return self.__toList(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Edit an existent 'Resenha' in the table ->
    def Edit(self, id, nome_review, review):
        db = PostgreDB()
        try:
            updating_query = f"update public.resenha set nome_review=%s, review=%s, date_register=CURRENT_TIMESTAMP" \
                             f" where id = {id}"
            db.queryParams(updating_query, (nome_review, review))
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Delete a resenha on DB ->
    def Delete(self, resenha_id):
        db = PostgreDB()
        try:
            db = PostgreDB()
            db.query(f"DELETE FROM public.resenha WHERE id = {resenha_id}")
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # Private Methods
    def __toList(self, review):
        def add(item):
            try:
                return self.__toOne(item)
            except Exception as exp:
                print(exp)

        try:
            return list(map(add, review))
        except Exception as exp:
            print(exp)

    def __toOne(self, item):
        try:
            return Resenha(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
        except Exception as exp:
            print(exp)

    def __toOneID(self, item):
        try:
            return ResenhaAuthorId(item[0])
        except Exception as exp:
            print(exp)
