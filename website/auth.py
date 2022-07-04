
import email
from flask import Blueprint, redirect, render_template, request, url_for, flash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET","POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    return render_template("login.html")

@auth.route("/signup", methods=["GET","POST"])
def sign_up():
    username = request.form.get("username")
    email = request.form.get("email")
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")
    
    return render_template("signup.html")

@auth.route("/logout")
def logout():
    flash("You have been logged out")
    return redirect(url_for("views.home"))

