from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from initialise import Initialise

def create_app(test_config=None):
    # Creates the Flask app
    init = Initialise()
    app = init.init(test_config)
    return app