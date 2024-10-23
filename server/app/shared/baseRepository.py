from app.shared.dataBase import db

class BaseRepository:
    
    def __init__(self, model):
        self.model = model 

    def save(self, object):
        db.session.add(object)
        db.session.commit()

    def update(self, object):
        object.verified = True
        db.session.commit()

    def delete(self, object):
        db.session.delete(object)
        db.session.commit()
        
    def get_all(self):
        return db.session.query(self.model).all()  # Retorna todos os objetos do modelo

    def get_by_id(self, id):
        return db.session.query(self.model).filter_by(id=id).first()  # Busca um objeto pelo ID