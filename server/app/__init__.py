import os
from flask import Flask
from flask_cors import CORS
from config import Config
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__,root_path=os.getcwd(), static_url_path='/static')
    app.config.from_object(Config)
    CORS(app)
    bcrypt.init_app(app)
    
    from app.shared.dataBase import db,migrate,marshmallow
    db.init_app(app)
    marshmallow.init_app(app)
    migrate.init_app(app, db)



    from app.routes.UserRoutes import user_bp
    app.register_blueprint(user_bp)
    
    return app