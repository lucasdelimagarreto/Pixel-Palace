
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

    def getById(self,id):
        try:
            object = db.get_or_404(self.model,id)
#TODO:tratamento de exeção para ser feito
        except:
            raise Exception()
        else:    
            return object
        
    def getAll(self):
        ...
