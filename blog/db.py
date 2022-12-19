import settings
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()

# Creates a data base
def create_database():
    db.create_all()
    print("Created database!")