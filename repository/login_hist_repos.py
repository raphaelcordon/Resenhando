from .base_repos import PostgreDB



class LoginHistRepository:

    # <- Register the time of the login in the table ->
    def New(self, user_id):
        db = PostgreDB()
        try:
            insert = f"INSERT INTO public.login_hist(user_id) VALUES (%s)"
            db.queryParams(insert, user_id)
        except Exception as exp:
            print(exp)
        finally:
            db.close()
