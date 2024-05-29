import os
from datetime import timedelta

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    JSON_SORT_KEYS=False
    JWT_SECRET_KEY='123456'
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(minutes=15)
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:123456@localhost:5432/pixel_palace"
    SQLALCHEMY_TRACK_MODIFICATIONS = False