from .base_repos import PostgreDB


class LoginHistRepository:

    # <- Register the time of the login in the table ->
    def New(self, user_id):
        db = PostgreDB()
        try:
            db.query(f"INSERT INTO public.login_hist(user_id) VALUES ({user_id})")
        except Exception as exp:
            print(exp)
        finally:
            db.close()

    # <- List last Two Logins ->
    def List(self, user_id):
        db = PostgreDB()
        try:
            db.query(f"SELECT * FROM public.login_hist WHERE USER_ID = {user_id} ORDER BY login_date DESC LIMIT 2")
            return self.__toList(db.fetchAll())
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
            return Users(item[0], item[1], item[2], item[3], item[4], item[5])
        except Exception as exp:
            print(exp)