from public.routes.mysqldb import mysql

def adding_contact(parameters = []):
    cur = mysql.connection.cursor()
    cur.callproc('add_contact', parameters)
    message = cur.fetchall()
    cur.nextset()
    mysql.connection.commit()
    return message[0][0]


def remove_contact(contact_id):
    cur = mysql.connection.cursor()
    cur.callproc('remove_contact', [contact_id, ])
    message = cur.fetchall()
    cur.nextset()
    mysql.connection.commit()
    return message[0][0]



def update_contact(parameters = []):
    cur = mysql.connection.cursor()
    cur.callproc('update_contact', parameters)
    message = cur.fetchall()
    cur.nextset()
    mysql.connection.commit()
    return message[0][0]

def getting_contact(contact_id):
    cur = mysql.connection.cursor()
    cur.callproc('get_contact', [contact_id, ])
    data = cur.fetchall()
    cur.nextset()
    return data[0]

def get_contacts(user_id):
    cur = mysql.connection.cursor()
    cur.nextset()
    cur.callproc('get_contacts', [
        user_id,
    ])
    data = cur.fetchall()
    cur.nextset()
    return data