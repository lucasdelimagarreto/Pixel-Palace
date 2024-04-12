from flask import Blueprint,jsonify,request,make_response
from app.repository.UserRepository import UserRepository
from app.shared.response import error_response,success_response
from app.service.UserService import UserService

user_bp = Blueprint('users_api',__name__,url_prefix='/users')
userService = UserService()

@user_bp.route("",methods=("GET", "POST","PUT","DELETE"))
def register():
    
    if request.method == "POST":
        
        if request.is_json:
            
            data = request.get_json()
            
            if len(data) < 3:
                return make_response(error_response(action="Register",error_code=400,error_message="missing one or more parameters"))
            
            elif len(data) > 3:
                return make_response(error_response(action="Register",error_code=400,error_message="too many parameters has been passed"))
            
            elif "username" not in data or "email" not in data or "password" not in data:
                return make_response(error_response(action="Register",error_code=400,error_message="error in json format"))
            
            else:
                username = data.get("username")
                email = data.get("email")
                password = data.get("password")
                
                try:
                    userService.findUserByUsername(username=username)
                
                except:
                    pass
                else:
                    return make_response(error_response(action="Register",error_message="Esse Username já foi cadastrado!",error_code=409))
                
                try:
                    userService.findUserByEmail(email=email)
                
                except:
                    pass
                
                else:                   
                    return make_response(error_response(action="Register",error_message="Esse e-mail já foi cadastrado",error_code=409))
                
                try:
                    userService.validate_new_user(username,email,password) 
                    response = userService.add_new_user(username=username,email=email,password=password)
                    return make_response(success_response(action="Register",parameter=response))           
                
                except Exception as err:
                    return make_response(error_response(action="Register",error_message=str(err),error_code=409))
                                                        
    return error_response(action="Register",error_code=400,error_message="error")