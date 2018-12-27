import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = False
TESTING = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = False
USE_RELOADER = False
ENV = 'production'
SCHEDULER_API_ENABLED = True
JOBS = [
        {
            'id': 'is_radio_playing',
            'func': 'radio_pi:is_radio_playing',
            'trigger': 'interval',
            'minutes': 1
        }
    ]
