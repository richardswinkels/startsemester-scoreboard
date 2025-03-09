import os
from models.db import db
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

    return app

app = create_app()
