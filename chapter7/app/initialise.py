class Initialise():

    def db(self, app):

        app.config.from_object("config.Config")

        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{}:{}@{}/{}'.format(
            app.config["DB_USERNAME"],
            app.config["DB_PASSWORD"],
            app.config["DB_LOCATION"],
            app.config["DB_DATABASE"]
        )
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        return app
