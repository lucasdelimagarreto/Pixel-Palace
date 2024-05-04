from app.model.User import User
from app.shared.baseRepository import BaseRepository
from app.shared.dataBase import db

class UserRepository(BaseRepository):

    def __init__(self):
        
        super().__init__(User)
    
    def getByUsername(self,username):
        
        try:
            user = db.session.execute(db.select(User).filter_by(username=username)).scalar_one()
        except:
            raise Exception("User not found")
        else:    
            return user
    
    def getByEmail(self,email):
        
        try:
            user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one()
        except:
            #TODO: traceback runtime error
            raise Exception("User not found")
        else:
            return user