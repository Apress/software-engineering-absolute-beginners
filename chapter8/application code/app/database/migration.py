from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import sys
sys.path.append("..")
from initialise import Initialise

# Creates the Flask app
app = Flask(__name__)
init = Initialise()
app = init.db(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

"""
Our data models
"""
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    surname = db.Column(db.String(128))
    identity_number = db.Column(db.Integer())

if __name__ == '__main__':
    manager.run()
