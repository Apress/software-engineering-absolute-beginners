from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import sys
sys.path.append("..")
from initialise import Initialise

app = Flask(__name__)
init = Initialise()
app = init.db(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

handler = Manager(app)
handler.add_command('db', MigrateCommand)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    surname = db.Column(db.String(128))
    identity_number = db.Column(db.Integer())

if __name__ == '__main__':
    handler.run()
