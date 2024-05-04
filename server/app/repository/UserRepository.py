from app.model.User import User
from app.shared.baseRepository import BaseRepository
from app.shared.dataBase import db

class UserRepository(BaseRepository):

    def __init__(self):
        super().__init__(User)
    
    def get_by_id(self, id):
        try:
            user = db.session.query(User).filter_by(id=id).first()
            if not user:
                raise Exception(f"No user found with id '{id}'")
            return user
        except Exception as e:
            raise e
    
    def get_by_username(self, username):
        try:
            user = db.session.query(User).filter_by(username=username).first()
            if not user:
                raise Exception(f"No user found with username '{username}'")
            return user
        except Exception as e:
            raise e
    
    def get_by_email(self, email):
        try:
            user = db.session.query(User).filter_by(email=email).first()
            if not user:
                raise Exception(f"No user found with email '{email}'")
            return user
        except Exception as e:
            raise e