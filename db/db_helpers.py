import db.db_connect as db

msdb = db.con()


class TryDBMessage:
    @staticmethod
    def message():  # <- Raise an error on the log if the table isn't found ->
        return f'The connection with the database filed.\n' \
               f" Make sure you have executed the script 'db_script.sql' in MySQL."


class DeletingDB:
    def __init__(self,table, item):   # <- Delete an user on DB ->
        try:
            cursor = msdb.cursor()
            cursor.execute("ROLLBACK")
            deleting_query = f"DELETE FROM public.{table} WHERE id='{item}'"
            cursor.execute(deleting_query)
            msdb.commit()
        except:
            TryDBMessage.message()
