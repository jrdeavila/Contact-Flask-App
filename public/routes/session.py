from flask import session
from public.flask_app import app


@app.before_request
def session_management():
    session.permanent = True

