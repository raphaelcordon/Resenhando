from .base_repos import PostgreDB
from models.users_model import Users


class UsersRepository:

    # <- Register a new 'User' in the table ->
    def New(self, name, surname, password, email):
        db = PostgreDB()
        try:
            insert = f"INSERT INTO public.users (name, surname, password, email, changepass)" \
                     f"VALUES (%s, %s, %s, %s, 'false')"
            db.queryParams(insert, (name, surname, password, email))
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Update User's password ->
    def UpdatePassword(self, id, new_password):
        db = PostgreDB()
        try:
            updating_query = f"UPDATE public.users SET PASSWORD=%s, CHANGEPASS=%s WHERE id = {id}"
            db.queryParams(updating_query, (new_password, 'false'))
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Reset User's password ->
    def ResetPassword(self, email, password):
        db = PostgreDB()
        try:
            updating_query = f"UPDATE public.users SET PASSWORD=%s, CHANGEPASS=%s WHERE EMAIL = '{email}'"
            db.queryParams(updating_query, (password, 'true'))
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- List USERS registered ->
    def List(self):
        db = PostgreDB()
        try:
            db.query(f"SELECT * FROM public.users")
            return self.__toList(db.fetchAll())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Update an existent User ->
    def Update(self, id, new_register, surname, email):
        db = PostgreDB()
        try:
            updating_query = f"UPDATE public.users SET NAME=%s, SURNAME=%s, EMAIL=%s WHERE id = {id}"
            db.queryParams(
                updating_query, (new_register, surname, email))
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- ID finder to redirect to resenhas page ->
    def FindById(self, id):
        db = PostgreDB()
        try:
            db.query(f"SELECT * FROM public.users where id = {id}")
            return self.__toOne(db.fetchOne())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    def FindByEmail(self, email):
        db = PostgreDB()
        try:
            db.query(f"SELECT * FROM public.users where email = '{email}'")
            return self.__toOne(db.fetchOne())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Delete an user on DB ->
    def Delete(self, id):
        db = PostgreDB()
        try:
            db.query(f"DELETE FROM public.users WHERE id = {id}")
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
            return Users(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
        except Exception as exp:
            print(exp)
