from flask_bcrypt import Bcrypt
from flask import Flask
from main.config import Config
from logger import StreamLogFormatter, FileLogFormatter
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
import logging
import os
import sys


bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "accounts.login"
login_manager.login_message_category = "warning"
migrate = Migrate(compare_type=True)


def create_app(config_class=Config):

    # basic configuration
    app = Flask(
        __name__,
        static_url_path="/static",
        static_folder="web/static",
        template_folder="web/templates"
    )

    # set up environment variables
    app.config.from_object(config_class)

    # password and form encryption
    bcrypt.init_app(app)

    # models
    from .modules.accounts import models
    from .modules.items import models
    from .modules.carts import models

    # database
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)

    # routes and blueprints
    from .modules.home.routes import home
    from .modules.accounts.routes import accounts
    from .modules.errors.handlers import errors
    from .modules.items.routes import items
    from .modules.carts.routes import carts

    for blueprint in [home, accounts, errors, items, carts]:
        app.register_blueprint(blueprint)

    # login manager
    login_manager.init_app(app)

    logger.info(f"Running app in environment '{os.environ.get('FLASK_ENV')}'")
    logger.info(f"SQLALCHEMY_DATABASE_URI: '{app.config.get('SQLALCHEMY_DATABASE_URI')}'")
    return app


# Set up logging
logging.basicConfig()
logger = logging.getLogger("ShoppingApp")
logger.propagate = False
sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(StreamLogFormatter())
fh = logging.FileHandler("application.log")
fh.setFormatter(FileLogFormatter())
logger.addHandler(sh)
logger.addHandler(fh)
logger.setLevel(logging.DEBUG if os.environ.get('FLASK_ENV') == "development" else logging.INFO)
