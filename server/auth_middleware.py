from functools import wraps
import jwt
from flask import request, abort,make_response
from flask import current_app
from app.shared.response import error_response
from app.service.UserService import UserService
userService = UserService()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        action = request.url.split("/")[3]
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return  make_response(error_response(action=action,error_message="Authentication Token is missing!",error_code=401,status="Unauthorized"))
        try:
            try:
                data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            except:
                raise Exception("Invalid Authentication token!",401)
            current_user = userService.get_user_by_id(data["id"])
        except Exception as err:
            if len(err.args) == 2:
                return make_response(error_response(action=action,status="Unauthorized",error_message=err.args[0],error_code=err.args[1]))
            else:
                return error_response(action=action,error_code=500,error_message=err.args)

        return f(current_user, *args, **kwargs)

    return decorated