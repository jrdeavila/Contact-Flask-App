from flask import render_template, request, redirect, url_for, flash
from hashlib import sha512
from public.flask_app import app
from public.routes.user import get_user, adding_user
from public.routes.session import session
from public.routes.contacts import get_contacts, adding_contact, remove_contact
from public.routes.contacts import update_contact, getting_contact


@app.route('/')
def Index():
    try:
        username = session["user"]
        auth = session["auth"]
    except:
        username = "unknown"
        auth = 0
    if auth == 0:
        print(auth)
        return render_template('index.html')
    else:
        return redirect(url_for('account', username=username))


@app.route('/signin')
def singin():
    return render_template('authentication/signin.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('Index'))


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        session.clear()
        session["user"] = request.form['username']
        session["password"] = request.form['password']
        query_result = get_user()

        if len(query_result[0]) > 1:
            session["auth"] = 1
        else:
            session["auth"] = 0
            flash(query_result[0][0])
        return Index()


@app.route('/signup')
def singup():
    return render_template('authentication/signup.html')


@app.route('/adduser', methods=['POST'])
def add_user():
    if request.method == 'POST':
        parameters = [
            request.form['firstname'],
            request.form['lastname'],
            request.form['phone'],
            request.form['username'],
            sha512(
                str(request.form['password']).encode()
            ).hexdigest()
        ]
        message = adding_user(parameters)
        flash(message)
        return redirect(url_for('singin'))


@app.route('/profile')
def profile():
    return redirect(url_for('account', username=session['user']))


@app.route('/<string:username>')
def account(username):
    user = get_user()
    return render_template('profile.html', user=user[0])


@app.route('/contacts')
def contacts():
    user = get_user()
    data = get_contacts(user[0][0])
    return render_template('contacts/contacts.html', contacts = data)


@app.route('/add')
def add():
    return render_template('contacts/add.html')


@app.route('/add_contact', methods = ['POST'])
def add_contact():
    if request.method == 'POST':
        import datetime
        user = get_user()
        parameters = [
            request.form['fullname'],
            request.form['phone'],
            request.form['email'],
            datetime.datetime.now(),
            user[0][0]
        ]
        message = adding_contact(parameters) 
        flash(message)
        return redirect(url_for('Index'))


@app.route('/delete/<string:id>')
def delete_contact(id):
    message = remove_contact(id)
    flash(message)
    return redirect(url_for('contacts'))


@app.route('/edit/<string:id>')
def get_contact(id):
    data = getting_contact(id)
    return render_template('contacts/edit.html', contact=data)


@app.route('/update/<string:id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        parameters = [
            request.form['fullname'],
            request.form['phone'],
            request.form['email'],
            id
        ]
        message = update_contact(parameters)
        flash(message)
        return redirect(url_for('Index'))


if __name__ == '__main__':
    app.run(host='192.168.1.54', debug=True, port='3000')
