from .base_repos import PostgreDB
from models.users_model import Users


class UsersRepository:

    # <- Register a new 'User' in the table ->
    def New(self, username, name, surname):
        db = PostgreDB()
        try:
            insert = f"INSERT INTO public.users (username, name, surname, password) VALUES (%s, %s, %s, 'pass')"
            db.queryParams(insert, (username, name, surname))
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Update User's password ->
    def UpdatePassword(self, id, new_password):
        db = PostgreDB()
        try:
            updating_query = f"UPDATE public.users SET PASSWORD=%s WHERE id = {id}"
            db.queryParams(updating_query, (new_password))
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Reset User's password ->
    def ResetPassword(self, username):
        db = PostgreDB()
        try:
            updating_query = f"UPDATE public.users SET PASSWORD=%s WHERE USERNAME = {username}"
            db.queryParams(updating_query, ('pass'))
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
    def Update(self, id, new_username, new_register, surname):
        db = PostgreDB()
        try:
            updating_query = f"UPDATE public.users SET USERNAME=%s, NAME=%s, SURNAME=%s WHERE id = {id}"
            db.queryParams(
                updating_query, (new_username, new_register, surname))
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

    # <- Username finder to redirect to resenhas page ->
    def FindByUsername(self, username):
        db = PostgreDB()
        try:
            db.query(f"SELECT * FROM public.users where username = '{username}'")
            return self.__toOne(db.fetchOne())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Delete an user on DB ->
    def Delete(self, id):
        db = PostgreDB()
        try:
            db = PostgreDB()
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
            return Users(item[0], item[1], item[2], item[3], item[4])
        except Exception as exp:
            print(exp)
