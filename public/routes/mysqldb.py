from public.flask_app import app
from flask_mysqldb import MySQL

# config mysql connection parameters
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'devcodehacker777'
app.config['MYSQL_PASSWORD'] = 'jose1003'
app.config['MYSQL_DB'] = 'mydb'

# settings
app.secret_key = 'mysecretkey'


mysql = MySQL(app)