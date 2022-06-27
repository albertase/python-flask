""" This will make this website folder a python package. that is the reason of creating this file."""

# Setting up  a flask app
from  flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    """The database is stored inside the website folder"""
    app = Flask(__name__)   # The name of the file
    app.config["SECRET_KEY"] = "KJJ"
    # app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://vvnufpmyatsyou:ba9e260081819be02d8c8eee49a3cd212577d5a92b0ed7dc353bdb87a9832381@ec2-52-72-99-110.compute-1.amazonaws.com:5432/deacbdgv1t53nc"
    db.init_app(app)
    
    
    from .views import  views
    from .auth import  auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    # import .models as models
    from .models import User, Note
    
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created database')
    