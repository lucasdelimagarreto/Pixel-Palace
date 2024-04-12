from app.model.Games import Games
from app.shared.baseRepository import BaseRepository
from app.shared.dataBase import db

class UserRepository(BaseRepository):

    def __init__(self):
        
        super().__init__(Games)
    
    def getByGamename(self,gameName):
        
        try:
            game = db.session.execute(db.select(Games).filter_by(username=gameName)).scalar_one()
        except:
            raise Exception("Game not found")
        else:    
            return game
    
    #def getByEmail(self,email):
    #    
    #    try:
    #        user = db.session.execute(db.select(Games).filter_by(email=email)).scalar_one()
    #    except:
    #        #TODO: traceback runtime error
    #        raise Exception("User not found")
    #    else:
    #        return user