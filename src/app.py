# src/app.py
import os

from flask import Flask
from flask_cors import CORS
import signal

from .config import app_config
from .models import db, bcrypt
from .controllers.ScreenshotController import screenshot_api
from .Core.screenshot_to_doc import ScreenshotToDoc

def create_app(env_name):
    """
    Documenting tool
  """

    # app initiliazation
    app = Flask(__name__)

    CORS(app)

    # class initialize
    app.config.from_object(app_config[env_name])


    # app.config['CACHE_TYPE'] = 'simple'
    # app.config['CACHE_DEFAULT_TIMEOUT'] = int(os.getenv("CACHE_DEFAULT_TIMEOUT"))

    # initializing bcrypt and db
    bcrypt.init_app(app)
    # db.init_app(app)

    app.register_blueprint(screenshot_api, url_prefix='/api/v1/screenshot')

    @app.route('/', methods=['GET'])
    def index():
        """
    test endpoint
    """
        return 'Welcome to Documenting Tool API'

    return app
