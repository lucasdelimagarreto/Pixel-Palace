import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    JSON_SORT_KEYS=False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a secret'
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:123456@localhost:5432/pixel_palace"
    SQLALCHEMY_TRACK_MODIFICATIONS = False