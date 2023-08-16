import os

from flask import Flask

from .extensions import db, migrate
from .routes import main
from .authroutes import auth
from .models import *


def create_app(database_uri="sqlite:///url_shortener.db"):

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SECRET_KEY"] = "secretkey"
    db.init_app(app)
    migrate.init_app(app, db)

    def bypass(env):
        return env['PATH_INFO'] == '/bypass'

    with app.app_context():
        db.create_all()

    app.register_blueprint(main)
    app.register_blueprint(auth)

    if __name__ == '__main__':
    # set this to '0.0.0.0' to bind to all interfaces
        hostname = os.environ.get('HOSTNAME', 'localhost')
        port = int(os.environ.get('PORT', 5000))
        debug = bool(os.environ.get('DEBUG', False))
        app.run(host=hostname, port=port, debug=debug)

    return app
