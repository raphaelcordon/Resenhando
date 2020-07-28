
from .base_repos import PostgreDB
from models.users_model import Users


class AuthenticateRepository:
    def auth(self, email):
        db = PostgreDB()
        try:
            db.query(
                f"SELECT * FROM public.users where EMAIL = '{email}'")
            return self.__toOne(db.fetchOne())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- Check if the there are comments and/or likes since last login ->
    def CompareDates(self, user_id):
        db = PostgreDB()
        try:
            db.query(f"SELECT login_date FROM public.login_hist where user_id = {user_id}"
                     f" ORDER BY login_date DESC LIMIT 1")
            return self.__toOne(db.fetchOne())
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # Private Methods
    def __toOne(self, item):
        try:
            return Users(item[0], item[1], item[2], item[3], item[4], item[5])
        except Exception as exp:
            print(exp)
