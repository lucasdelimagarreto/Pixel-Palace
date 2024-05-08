from app.shared.dataBase import db

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer ,primary_key=True,autoincrement=True)
    username = db.Column(db.String(20), unique=True , nullable=False)
    email = db.Column(db.String(40), unique=True , nullable=False)
    password = db.Column(db.String , nullable=False)
    age = db.Column(db.String(20) ,nullable=False)

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password