import psycopg2


msdb = psycopg2.connect(
    host='ec2-54-75-246-118.eu-west-1.compute.amazonaws.com',
    database='d89gkq7l8caqks',
    user='xcdauuhtrmsrhw',
    port='5432',
    password='b6e8f984b04f80bf4311d33f68a2e6c04ce062540161e7f092c3b047c4cca9e5',
)


# <--- Authentication DEFs beginning --->

def authenticate(username):
    try:
        cursor = msdb.cursor()
        cursor.execute("ROLLBACK")
        cursor.execute(f"SELECT * FROM public.users where username = '{username}'")
        find = cursor.fetchone()
        return Users(find[0], find[1], find[2], find[3], find[4], find[5])
    except:
        TryDBMessage.message()


# <--- Authentication DEFs Ending --->


# <--- Course DEFs beginning --->

def course_list():  # <- List Courses on Courses Page ->
    cursor = msdb.cursor()
    cursor.execute("ROLLBACK")
    cursor.execute(f"SELECT * FROM public.course")
    course = translate_courses(cursor.fetchall())
    return course