from flask import Flask, session, request, redirect, get_flashed_messages
from .exceptions import InvalidCredentials, handler_invalid_credentials, TooManyAttempt

app = Flask(__name__)

app.register_error_handler(InvalidCredentials, handler_invalid_credentials)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.get('/')
def home():
    if 'username' in session:
        return f'Hello, {session["username"]}! <a href="/logout">Logout</a>'
    return redirect('/login')

@app.get('/login')
def login_form():
    html = ''
    
    if len(get_flashed_messages()) > 0:
        html += f"<h2>{get_flashed_messages()[0]}</h2>"
    
    html += '''
    <form action="/login" method="post">
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <input type="submit">
    </form>'''
    return html

@app.post('/login')
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'hansen' and password == 'hansgans':
        session['username'] = username
        return redirect('/')
    else:
        session[f'attempt_{username}'] = session.get(f'attempt_{username}', 0) + 1
        if session[f'attempt_{username}'] >= 3:
            raise TooManyAttempt
        raise InvalidCredentials
    
@app.get('/logout')
def logout():
    session.clear()
    return redirect('/login')