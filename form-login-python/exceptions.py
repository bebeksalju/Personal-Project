from werkzeug.exceptions import HTTPException
from flask import redirect, flash

class InvalidCredentials(HTTPException):
    code = 401
    description = 'Invalid credentials, please try again'

def handler_invalid_credentials(e: InvalidCredentials):
    flash(e.description, "Error")
    return redirect('/login')

class TooManyAttempt(HTTPException):
    code = 429
    description = 'Too many attempts, try again later'