from app.model.Games import Games
from app.shared.baseRepository import BaseRepository
from app.shared.dataBase import db

class GamesRepository(BaseRepository):

    def __init__(self):
        
        super().__init__(Games)
    
    def getByGamename(self,gameName):
        
        try:
            game = db.session.execute(db.select(Games).filter_by(gameName=gameName)).scalar_one()
        except:
            raise Exception("Game not found")
        else:    
            return game
    
    def getByGender(self,gender):
        
        try:
            game = db.session.execute(db.select(Games).filter_by(gender=gender)).scalar_one()
        except:
            #TODO: traceback runtime error
            raise Exception("gender not found")
        else:
            return game
    
    def getById(self, id):
        
        try:
            game = db.session.execute(db.select(Games).filter_by(id=id)).scalar_one()
        except:
            raise Exception("Id not found")
        else:
            return game
        
    def getBySecondGameName(self, secondGameName):
        
        try:
            game = db.session.execute(db.select(Games).filter_by(secondGameName=secondGameName)).scalar_one()
        except:
            #TODO: traceback runtime error
            raise Exception("secondGameName not found")
        else:
            return game
        
    def getByCreator(self, creator):
        
        try:
            game = db.session.execute(db.select(Games).filter_by(creator=creator)).scalar_one()
        except:
            #TODO: traceback runtime error
            raise Exception("secondGameName not found")
        else:
            return game
        
    def getByYear(self, year):
        
        try:
            game = db.session.execute(db.select(Games).filter_by(year=year)).scalar_one()
        except:
            #TODO: traceback runtime error
            raise Exception("secondGameName not found")
        else:
            return game