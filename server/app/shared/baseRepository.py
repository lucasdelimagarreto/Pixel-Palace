
from app.shared.dataBase import db

class BaseRepository:
    
    def __init__(self,model):
        self.model = model 
        

    def save(self,object):
        db.session.add(object)
        db.session.commit()


    def getById(self,id):
        object = db.get_or_404(self.model,id)
        return object
        
