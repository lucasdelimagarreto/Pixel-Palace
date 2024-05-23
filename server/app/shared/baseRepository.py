from app.shared.dataBase import db

class BaseRepository:
    
    def __init__(self,model):
        self.model = model 

    def save(self,object):
        db.session.add(object)
        db.session.commit()

    def update(self,object):
        object.verified = True
        db.session.commit()

    def delete(self,object):
        db.session.delete(object)
        db.session.commit()
        
    def getAll(self):
        ...