import os
from models.db import db
from werkzeug.middleware.proxy_fix import ProxyFix
from controllers.player_controller import player_controller
from controllers.score_controller import score_controller
from controllers.api_score_controller import api_score_controller
from dotenv import load_dotenv
from flask import Flask

def create_app():
    app = Flask(__name__)

    load_dotenv(override=True)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['MICROCONTROLLER_BASE_URL'] = os.getenv('MICROCONTROLLER_BASE_URL')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(player_controller)
    app.register_blueprint(score_controller)
    app.register_blueprint(api_score_controller)

    return app

app = create_app()
