
from .base_repos import PostgreDB
from models.users_model import Users


class AuthenticateRepository:
    def auth(self, username):
        db = PostgreDB()
        try:
            db.query(f"SELECT * FROM public.users where username = '{username}'")
            return self.__toOne(db.fetchOne())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # Private Methods
    def __toOne(self, item):
        try:
            return Users(item[0], item[1], item[2], item[3], item[4])
        except Exception as exp:
            print(exp)