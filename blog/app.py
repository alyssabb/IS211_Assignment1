import settings

import os
from os import path
from flask import Flask
from db import db, create_database
from users.views import get_auth_routes
from posts.views import get_post_views
from users.login_manager import create_login_manager
from users.utils import create_demo_user


def build_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "hakldfhlahf"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{settings.DB_NAME}'
    db.init_app(app)
    
    # Checks the existance of the sqlite file 
    # If no file is found, creates a db and a demo user
    with app.app_context():
        if not path.exists(os.getcwd() + "/instance/" + settings.DB_NAME):
            create_database()
            create_demo_user(db)
    
    # Loads the user routes
    app = get_auth_routes(app)
    
    # Loads the posts routes
    app = get_post_views(app)
    
    # Useful to handle user login and logout
    create_login_manager(app)
    
    return app

if __name__ == "__main__":
    app = build_app()
    app.run(debug=True)
