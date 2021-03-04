from public.routes.mysqldb import  mysql
from public.routes.session import session
from hashlib import sha512

def get_user():
    cur = mysql.connection.cursor()
    cur.callproc('get_user', [
        session['user'],
        sha512(str(session['password']).encode()).hexdigest()
    ])
    query_result = cur.fetchall()
    cur.nextset()

    return query_result

def adding_user(parameters = []):
    cur = mysql.connection.cursor()
    cur.callproc('add_user', parameters)
    message = cur.fetchall()
    cur.nextset()
    mysql.connection.commit()
    return message[0][0]