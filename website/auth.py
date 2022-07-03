from flask import Blueprint, redirect, render_template, url_for

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/signup")
def sign_up():
    return render_template("signup.html")

@auth.route("/logout")
def logout():
    return render_template("index.html",alert="logged_out")

