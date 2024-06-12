from app.shared.dataBase import db

class Games(db.Model):

    __tablename__ = "games"

    id = db.Column(db.Integer ,primary_key=True,autoincrement=True)
    gameName = db.Column(db.String(20), nullable=False)
    secondGameName = db.Column(db.String(20), nullable=False)
    creator = db.Column(db.String(30), nullable=False)
    publisher = db.Column(db.String(30), nullable=True)
    price = db.Column(db.String(15))
    year = db.Column(db.Integer, nullable=False)
    dlc = db.Column(db.Boolean)
    gender = db.Column(db.String(20), nullable=False)
    ageGroup = db.Column(db.Integer , nullable=False)
    platform = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(500), nullable=False) #Isso e sujo mas e o que temos para hoje, PS esta marcação e um lembrete para fazer uma alteração!
    imageBanner = db.Column(db.String(200), nullable=True)
    videoPromotional = db.Column(db.String(200), nullable=True)
    
    def __init__(self,gameName, secondGameName, creator, publisher, price, year, dlc, gender, ageGroup, platform, description, imageBanner, videoPromotional):
        self.gameName = gameName
        self.secondGameName = secondGameName
        self.creator = creator
        self.publisher = publisher
        self.price = price
        self.year = year
        self.dlc = dlc
        self.gender = gender
        self.ageGroup = ageGroup
        self.platform = platform
        self.description = description
        self.imageBanner = imageBanner
        self.videoPromotional = videoPromotional
        
    def to_dict(self):
        return {
            "id": self.id,
            "gameName": self.gameName,
            "secondGameName": self.secondGameName,
            "creator": self.creator,
            "publisher": self.publisher,
            "price": self.price,
            "year": self.year,
            "dlc": self.dlc,
            "gender": self.gender,
            "ageGroup": self.ageGroup,
            "platform": self.platform,
            "description": self.description,
            "imageBanner": self.imageBanner,
            "videoPromotional": self.videoPromotional
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            gameName=data.get("gameName"),
            secondGameName=data.get("secondGameName"),
            creator=data.get("creator"),
            publisher=data.get("publisher"),
            price=data.get("price"),
            year=data.get("year"),
            dlc=data.get("dlc"),
            gender=data.get("gender"),
            ageGroup=data.get("ageGroup"),
            platform=data.get("platform"),
            description=data.get("description"),
            imageBanner=data.get("imageBanner"),
            videoPromotional=data.get("videoPromotional")
        )