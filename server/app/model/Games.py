from app.shared.dataBase import db

class Games(db.Model):

    __tablename__ = "games"

    id = db.Column(db.Integer ,primary_key=True,autoincrement=True)
    gameName = db.Column(db.String(20), nullable=False)
    secondGameName = db.Column(db.String(20), nullable=False)
    creator = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float)
    year = db.Column(db.Integer , nullable=False)
    dlc = db.Column(db.Boolean)
    gender = db.Column(db.String(20), nullable=False)
    ageGroup = db.Column(db.Integer , nullable=False)
    platform = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(50), nullable=False) #Isso e sujo mas e o que temos para hoje, PS esta marcação e um lembrete para fazer uma alteração!

    def __init__(self,gameName, secondGameName, creator, price, year, dlc, gender, ageGroup, platform, description):
        self.gameName = gameName
        self.secondGameName = secondGameName
        self.creator = creator
        self.price = price
        self.year = year
        self.dlc = dlc
        self.gender = gender
        self.ageGroup = ageGroup
        self.platform = platform
        self.description = description