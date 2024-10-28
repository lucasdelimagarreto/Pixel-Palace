from app.shared.dataBase import db
from app.model.UserGames import user_games
from app.model.Games import Games

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer ,primary_key=True,autoincrement=True)
    username = db.Column(db.String(20), unique=True , nullable=False)
    email = db.Column(db.String(40), unique=True , nullable=False)
    password = db.Column(db.String , nullable=False)
    age = db.Column(db.String(20) ,nullable=False)
    patent = db.Column(db.Integer ,nullable=False)
    favorite_games = db.relationship('Games', secondary=user_games,back_populates='user')

    def __init__(self,username,email,password,patent = None):
        self.username = username
        self.email = email
        self.password = password
        self.patent = 1 if patent == None else patent
        