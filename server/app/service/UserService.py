from app.shared.validation_methods import validate_username, validate_email, validate_password
from app.model.User import User
from app.schemas.UserSchema import UserSchema
from app.repository.UserRepository import UserRepository

users = User(username=None,email=None,password=None)
userSchema = UserSchema()
userRepository = UserRepository()

class UsernameTakenError(Exception):
    pass

class EmailTakenError(Exception):
    pass

class InvalidDataError(Exception):
    pass

class UserService:
    
    def __init__(self, userRepository: UserRepository) -> None:
        self.userRepository = userRepository
    
    def add_new_user(self, username, email, password):
        try:
            validate_username(username)
            validate_email(email)
            validate_password(password)
            
            existing_user = self.userRepository.get_by_username(username)
            if existing_user:
                raise UsernameTakenError(f"The username '{username}' is already taken")
            
            existing_user = self.userRepository.get_by_email(email)
            if existing_user:
                raise EmailTakenError(f"The email '{email}' is already registered")
            
            user = User(username=username, email=email, password=password)
            self.userRepository.save(user)
            
            return {"success": True, "user": userSchema.dump(user)}
        
        except (UsernameTakenError, EmailTakenError, InvalidDataError) as e:
            return {"success": False, "error_message": str(e)}
    
    def find_user_by_id(self, id):
        user = self.userRepository.get_by_id(id=id)
        return user
    
    def find_user_by_username(self, username):
        user = self.userRepository.get_by_username(username=username)
        return user
    
    def find_user_by_email(self, email):
        user = self.userRepository.get_by_email(email=email)
        return user