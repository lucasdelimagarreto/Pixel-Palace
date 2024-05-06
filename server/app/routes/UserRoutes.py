from flask import Blueprint,jsonify,request,make_response,current_app
from app.shared.validation_methods import validate_password
from app.shared.response import error_response,success_response
from app.service.UserService import UserService
import jwt

user_bp = Blueprint('users_api',__name__,url_prefix='/users')
userService = UserService()

@user_bp.route("",methods=["GET","POST"])
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
                    userService.validate_new_username(username=username)
                    userService.validate_new_email(email=email)
                    validate_password(password=password)
                    userService.add_new_user(username=username,email=email,password=password)
                    return make_response(success_response(action="Register"))           
                except Exception as err:
                    if len(err.args) == 2:
                        return make_response(error_response(action="Register",error_message=err.args[0],error_code=err.args[1]))
                    else:
                        return make_response(error_response(action="Register",error_message=str(err),error_code=500))
        else:
            #TODO:arrumar esse bad request                                                                                
            return make_response(error_response(action="Register",error_message="Bad Request",error_code=400))                                                    


@user_bp.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        if request.is_json:
            data = request.json
            if len(data) < 2:
                return make_response(error_response(action="Authenticate",error_code=400,error_message="missing one or more parameters"))
            elif len(data) > 2:
                return make_response(error_response(action="Authenticate",error_code=400,error_message="too many parameters has been passed"))
            elif "username" not in data or "password" not in data:
                return make_response(error_response(action="Authenticate",error_code=400,error_message="error in json format"))
            username = data.get("username")
            password = data.get("password")
            try:
                user = userService.authenticate_user(username=username,password=password)
                token = jwt.encode({"id": user["id"]},current_app.config["SECRET_KEY"],algorithm="HS256")
                user.pop("id")
                return  make_response(success_response(action="Authenticate",token=token, parameter=user))        
            except Exception as err:
                if len(err.args) == 2:
                        return make_response(error_response(action="Authenticate",error_message=err.args[0],error_code=err.args[1]))
                else:
                    return error_response(action="Authenticate",error_code=500,error_message=err.args)
        else:
            #TODO:arrumar esse bad request   
            return error_response(action="Authenticate",error_code=400,error_message="Bad Request")