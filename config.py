import os


class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USE_RELOADER = False
    ENV = 'development'
