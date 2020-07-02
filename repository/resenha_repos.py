from .base_repos import PostgreDB
from models.resenha_model import Resenha, ResenhaCapa


class ResenhaRepository:

    def List(self):
        db = PostgreDB()
        try:
            db.query(f"SELECT * FROM public.resenha")
            return self.__toList(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Register a new 'Resenha' in the table ->
    def New(self, tipo_review, author_id, spotify_link, nome_review, nome_banda, review, date_register, image_file):
        db = PostgreDB()
        try:
            insert = f"INSERT INTO public.resenha (tipo_review, author_id, spotify_link, nome_review, nome_banda, review, date_register, image_file) " \
                f"VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            db.queryParams(insert, (tipo_review, author_id, spotify_link,
                                    nome_review, nome_banda, review, date_register, image_file))
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

    # <- ID finder to redirect to Edit page ->
    def FindCapaById(self, id):
        db = PostgreDB()
        try:
            db.query(f"SELECT image_file FROM public.resenha where id = {id}")
            return ResenhaCapa(db.fetchOne())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Register a new 'Resenha' in the table ->
    def Edit(self, id, tipo_review, spotify_link, nome_review, nome_banda, review, date_register, image_file):
        db = PostgreDB()
        try:
            updating_query = f"update public.resenha set tipo_review=%s, spotify_link=%s, " \
                f"nome_review=%s, nome_banda=%s, review=%s, date_register=%s, image_file=%s where id = {id}"
            db.queryParams(updating_query, (tipo_review, spotify_link,
                                            nome_review, nome_banda, review, date_register, image_file))
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Delete a resenha on DB ->
    def Delete(self, resenha_id):
        try:
            db = PostgreDB()
            db.query(f"DELETE FROM public.resenha WHERE id = {resenha_id}")
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # Private Methods
    def __toList(self, resenha):
        def add(item):
            try:
                return self.__toOne(item)
            except Exception as exp:
                print(exp)

        try:
            return list(map(add, resenha))
        except Exception as exp:
            print(exp)

    def __toOne(self, item):
        try:
            return Resenha(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8])
        except Exception as exp:
            print(exp)
