from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return "<h1>This is Login Page</h1>"

@auth.route("/signup")
def sign_up():
    return "<h1>This is Sign Up</h1>"

@auth.route("/logout")
def logout():
    return "<h1>This is Logout Page</h1>"

