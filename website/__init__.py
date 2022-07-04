from calendar import c
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "secretkey"
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    from .models import User
    
    create_database(app)
    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    
    return app
    
def create_database(app):
    if not path.exists("website/"+DB_NAME):
        db.create_all(app=app)
        print("Database Created!")