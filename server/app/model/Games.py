from app.shared.dataBase import db

class Games(db.Model):

    __tablename__ = "games"

    id = db.Column(db.Integer ,primary_key=True,autoincrement=True)
    gameName = db.Column(db.String(20), unique=True , nullable=False)
    secondGameName = db.Column(db.String(20), unique=True , nullable=False)
    creator = db.Column(db.String(10), unique=True , nullable=False)
    price = db.Column(db.Float , nullable=False)
    year = db.Column(db.Integer , nullable=False)
    dlc = db.Column(db.Boolean , nullable=False)
    gender = db.Column(db.String(20), nullable=False)

    def __init__(self,gameName, secondGameName, creator, price, year, dlc, gender):
        self.gameName = gameName
        self.secondGameName = secondGameName
        self.creator = creator
        self.price = price
        self.year = year
        self.dlc = dlc
        self.gender = gender