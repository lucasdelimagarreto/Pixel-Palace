import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    JSON_SORT_KEYS=False
    
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@localhost:5432/MyHO"
    SQLALCHEMY_TRACK_MODIFICATIONS = False