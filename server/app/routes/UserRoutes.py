from flask import Blueprint, jsonify, request, make_response
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from app.shared.validation_methods import validate_password
from app.shared.response import error_response, success_response
from app.service.UserService import UserService

user_bp = Blueprint('users_bp', __name__, url_prefix='/users')
userService = UserService()

@user_bp.route("", methods=["POST"])
def register():
    if request.method == "POST":
        if request.is_json:
            data = request.get_json()
            if len(data) < 4:
                return make_response(error_response(action="Register", error_code=400, error_message="missing one or more parameters"))
            elif len(data) > 4:
                return make_response(error_response(action="Register", error_code=400, error_message="too many parameters have been passed"))
            elif "username" not in data or "email" not in data or "password" not in data or "age" not in data:
                return make_response(error_response(action="Register", error_code=400, error_message="error in json format"))
            else:
                username = data.get("username")
                email = data.get("email")
                password = data.get("password")
                age = data.get("age")
                try:
                    userService.validate_new_username(username=username)
                    userService.validate_new_email(email=email)
                    validate_password(password=password)
                    userService.add_new_user(username=username, email=email, password=password, age=age)
                    return make_response(success_response(action="Register"))
                except Exception as err:
                    if len(err.args) == 2:
                        return make_response(error_response(action="Register", error_message=err.args[0], error_code=err.args[1]))
                    else:
                        return make_response(error_response(action="Register", error_message=str(err), error_code=409))
        else:
            return make_response(error_response(action="Register", error_message="Bad Request", error_code=409))

@user_bp.route("", methods=["GET"])
def get_user():
    user_id = request.args.get('user_id')
    username = request.args.get('username')
    email = request.args.get('email')

    try:
        if user_id:
            user = userService.get_user_by_id(int(user_id))
        elif username:
            user = userService.get_user_by_username(username)
        elif email:
            user = userService.get_user_by_email(email)
        else:
            return make_response(error_response(action="ObterUsuário", error_code=400, error_message="Parâmetro de consulta ausente"))

        if user:
            user_dict = user.__dict__
            user_dict.pop('_sa_instance_state')  # Remover atributo específico que não precisa ser serializado
            return make_response(success_response(action="ObterUsuário", user=user_dict))
        else:
            return make_response(error_response(action="ObterUsuário", error_code=404, error_message="Usuário não encontrado"))
    except Exception as err:
        return make_response(error_response(action="ObterUsuário", error_code=500, error_message=str(err)))

@user_bp.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        if request.is_json:
            data = request.json
            if len(data) < 2:
                return make_response(error_response(action="Authenticate", error_code=400, error_message="missing one or more parameters"))
            elif len(data) > 2:
                return make_response(error_response(action="Authenticate", error_code=400, error_message="too many parameters have been passed"))
            elif "email" not in data or "password" not in data:
                return make_response(error_response(action="Authenticate", error_code=400, error_message="error in json format"))

            email = data.get("email")
            password = data.get("password")
            try:
                user = userService.authenticate_user(email=email, password=password)
                access_token = create_access_token(identity=email)
                user.pop("id")  # Assuming you want to exclude 'id' from the response
                return make_response(success_response(action="Authenticate", access_token=access_token, user=user))
            except Exception as err:
                if len(err.args) == 2:
                    return make_response(error_response(action="Authenticate", error_message=err.args[0], error_code=err.args[1]))
                else:
                    return make_response(error_response(action="Authenticate", error_code=500, error_message=str(err)))
        else:
            return error_response(action="Authenticate", error_code=400, error_message="Bad Request")

@user_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@user_bp.route("", methods=["PATCH"])
@jwt_required()
def user_methods():
    current_user_email = get_jwt_identity()
    current_user = userService.get_user_by_email(current_user_email)
    
    if request.method == "PATCH":
        if request.is_json:
            data = request.json
            if len(data) < 1:
                return make_response(error_response(action="Update User Info", error_code=400, error_message="missing one or more parameters"))
            elif len(data) > 1:
                return make_response(error_response(action="Update User Info", error_code=400, error_message="too many parameters have been passed"))
            elif "username" not in data and "email" not in data and "password" not in data:
                return make_response(error_response(action="Update User Info", error_code=400, error_message="error in json format"))
            else:
                if "username" in data:
                    try:
                        username = data.get("username")
                        userService.validate_new_username(username=username)
                        userService.update_username(user_id=current_user['id'], username=username)
                        return make_response(success_response(action="Set New Username"))
                    except Exception as err:
                        if len(err.args) == 2:
                            return make_response(error_response(action="Set New Username", error_message=err.args[0], error_code=err.args[1]))
                        else:
                            return make_response(error_response(action="Set New Username", error_message=str(err), error_code=500))

                elif "email" in data:
                    try:
                        email = data.get("email")
                        userService.validate_new_email(email=email)
                        userService.update_email(user_id=current_user['id'], email=email)
                        return make_response(success_response(action="Set New E-mail"))
                    except Exception as err:
                        if len(err.args) == 2:
                            return make_response(error_response(action="Set New E-mail", error_message=err.args[0], error_code=err.args[1]))
                        else:
                            return make_response(error_response(action="Set New E-mail", error_message=str(err), error_code=500))

                elif "password" in data:
                    try:
                        password = data.get("password")
                        validate_password(password=password)
                        userService.update_password(user_id=current_user['id'], password=password)
                        return make_response(success_response(action="Set New Password"))
                    except Exception as err:
                        if len(err.args) == 2:
                            return make_response(error_response(action="Set New Password", error_message=err.args[0], error_code=err.args[1]))
                        else:
                            return make_response(error_response(action="Set New Password", error_message=str(err), error_code=500))
        else:
            return error_response(action="Update User Info", error_code=400, error_message="Bad Request")