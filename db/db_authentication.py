import db.db_connect as db
from db.db_helpers import TryDBMessage
from models import Users

msdb = db.con()


#   <--- Authentication DEFs beginning --->

def authenticate(username):
    try:
        cursor = msdb.cursor()
        cursor.execute("ROLLBACK")
        cursor.execute(f"SELECT * FROM public.users where username = '{username}'")
        find = cursor.fetchone()
        return Users(find[0], find[1], find[2], find[3], find[4])
    except:
        TryDBMessage.message()

# <--- Authentication DEFs Ending --->
