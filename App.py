from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# config mysql connection parameters

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'devcodehacker777'
app.config['MYSQL_PASSWORD'] = 'jose1003'
app.config['MYSQL_DB'] = 'mydb'

# settings
app.secret_key = 'mysecretkey'

mysql = MySQL(app)

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacs')
    data = cur.fetchall()
    
    return render_template('index.html', contacts = data)

@app.route('/add_contact', methods = ['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        tuple_data = (fullname, phone, email)
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacs(fullname, phone, email) VALUES (%s, %s, %s)', tuple_data)
        mysql.connection.commit()
        flash('contact added successfully')        
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacs WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('contact deleted successfully')
    return redirect(url_for('Index'))

@app.route('/edit/<string:id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacs WHERE id = {0}'.format(id))
    data = cur.fetchall()
    return render_template('edit.html', contact = data[0])

@app.route('/update/<string:id>', methods = ['POST'])
def update(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        tuple_data = (fullname, phone, email, id)
        cur = mysql.connection.cursor()
        cur.execute("""
                UPDATE contacs
                SET fullname = %s,
                phone = %s,
                email = %s
                WHERE id = %s
                """, tuple_data)
        mysql.connection.commit()
        flash('contact updated successfully')
        return redirect(url_for('Index'))


if __name__ == '__main__':
    app.run(port = 3000, debug = True)
