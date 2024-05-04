
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
marshmallow = Marshmallow()
migrate = Migrate()
