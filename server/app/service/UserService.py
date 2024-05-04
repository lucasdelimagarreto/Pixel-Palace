from app import bcrypt
from app.shared.validation_methods import validate_username, validate_email, validate_password
from app.model.User import User
from app.schemas.UserSchema import UserSchema
from app.repository.UserRepository import UserRepository

userSchema = UserSchema()
userRepository = UserRepository()

class UsernameTakenError(Exception):
    pass

class EmailTakenError(Exception):
    pass

class InvalidDataError(Exception):
    pass

class UserService:
    
    def __init__(self) -> None:
        pass
    
    def add_new_user(self,username,email,password):
        user = User(username=None,email=None,password=None)
        user.username = username         
        user.email = email         
        user.password =  bcrypt.generate_password_hash(password).decode("utf-8")         
        userRepository.save(user)         
        return
    
    def find_user_by_id(self, id):
        user = userRepository.get_by_id(id=id)
        return user
    
    def find_user_by_username(self, username):
        user = userRepository.get_by_username(username=username)
        return user
    
    def find_user_by_email(self, email):
        user = userRepository.get_by_email(email=email)
        return user
    
    # Erro nos metodos de validação e username e email
    def validate_new_username(self,username):
        validate_username(username)
        user = userRepository.get_by_username(username=username)
        if user != None:
            raise Exception("Esse Username já foi cadastrado!",409)
        pass
        
    def validate_new_email(self,email):
        validate_email(email)
        user = userRepository.get_by_email(email=email)
        if user != None:
            raise Exception("Esse e-mail já foi cadastrado",409)
        pass

    def authenticate_user(self,username,password):
        user = userRepository.get_by_username(username=username)
        if user == None:
            raise Exception("Usuário e/ou senha inválidos",401)
        if not bcrypt.check_password_hash(user.password, password):
            raise Exception("Usuário e/ou senha inválidos",401)
        user = userSchema.dump(user)
        user.pop("password")
        user.pop("posts")
        return user