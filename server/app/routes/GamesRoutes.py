from flask import Blueprint,jsonify,request,make_response
from app.shared.response import error_response,success_response
from app.service.GamesService import GamesService
from flask_jwt_extended import get_jwt_identity, jwt_required

games_bp = Blueprint('games_api',__name__,url_prefix='/games')
gamesService = GamesService()

@games_bp.route("", methods=["POST"])
@jwt_required()
def register():
    current_user = get_jwt_identity()

    if current_user != "teste@teste.com":
        return make_response(error_response(action="Verification", error_code=403, error_message="User does not have permission"))

    else:

        if request.method == "POST":
            if request.is_json:
                data = request.get_json()

                required_params = ["gameName", "secondGameName", "creator", "price", "year", "dlc", "gender", "ageGroup", "platform", "description"]
                if not all(param in data for param in required_params):
                    return make_response(error_response(action="Register", error_code=400, error_message="One or more parameters are missing"))

                try:
                    gamesService.get_game_by_name(gameName=data["gameName"])
                except:
                    pass
                else:
                    return make_response(error_response(action="Register", error_message="This game has already been registered!", error_code=409))

                try:
                    gamesService.validate_new_game(data["gameName"], data["secondGameName"], data["creator"], data["price"], data["year"], data["dlc"], data["gender"], data["ageGroup"], data["platform"], data["description"])
                    response = gamesService.add_new_game(gameName=data["gameName"], secondGameName=data["secondGameName"], creator=data["creator"], price=data["price"], year=data["year"], dlc=data["dlc"], gender=data["gender"], ageGroup=data["ageGroup"], platform=data["platform"], description=data["description"])
                    return make_response(success_response(action="Register", parameter=response))
                except Exception as err:
                    return make_response(error_response(action="Register", error_message=str(err), error_code=410))

    return error_response(action="Register", error_code=400, error_message="Error")

# Métodos GET para obter um jogo
@games_bp.route("/filter", methods=["GET"])
def get_game_by_name():

    if "game_id" in request.args:
        game_id = request.args.get("game_id")
        try:
            game = gamesService.get_game_by_id(game_id)
            if game:
                return jsonify({"status": "success", "action": "Get Game By Id", "game": game})
            else:
                return jsonify({"status": "error", "action": "Get Game By Id", "error_message": "Game not found"}), 404
        except Exception as err:
            return jsonify({"status": "error", "action": "Get Game By Id", "error_message": str(err)}), 500

    elif "game_name" in request.args:
        game_name = request.args.get("game_name")
        try:
            game = gamesService.get_game_by_name(game_name)
            if game:
                return jsonify({"status": "success", "action": "Get Game By Name", "game": game})
            else:
                return jsonify({"status": "error", "action": "Get Game By Name", "error_message": "Game not found"}), 404
        except Exception as err:
            return jsonify({"status": "error", "action": "Get Game By Name", "error_message": str(err)}), 500

    elif "game_gender" in request.args:
        game_gender = request.args.get("game_gender")
        try:
            game = gamesService.get_game_by_gender(game_gender)
            if game:
                return jsonify({"status": "success", "action": "Get Game By Gender", "game": game})
            else:
                return jsonify({"status": "error", "action": "Get Game By Gender", "error_message": "Game not found"}), 404
        except Exception as err:
            return jsonify({"status": "error", "action": "Get Game By Gender", "error_message": str(err)}), 500

    elif "game_creator" in request.args:
        game_creator = request.args.get("game_creator")
        try:
            game = gamesService.get_game_by_creator(game_creator)
            if game:
                return jsonify({"status": "success", "action": "Get Game By creator", "game": game})
            else:
                return jsonify({"status": "error", "action": "Get Game By creator", "error_message": "Game not found"}), 404
        except Exception as err:
            return jsonify({"status": "error", "action": "Get Game By creator", "error_message": str(err)}), 500

    elif "game_year" in request.args:
        game_year = request.args.get("game_year")
        try:
            game = gamesService.get_game_by_year(game_year)
            if game:
                return jsonify({"status": "success", "action": "Get Game By Year", "game": game})
            else:
                return jsonify({"status": "error", "action": "Get Game By Year", "error_message": "Game not found"}), 404
        except Exception as err:
            return jsonify({"status": "error", "action": "Get Game By Year", "error_message": str(err)}), 500

    elif "age_group" in request.args:
        age_group = request.args.get("age_group")
        try:
            game = gamesService.get_game_by_age_group(age_group)
            if game:
                return jsonify({"status": "success", "action": "Get Game By Age group", "game": game})
            else:
                return jsonify({"status": "error", "action": "Get Game By Age group", "error_message": "Game not found"}), 404
        except Exception as err:
            return jsonify({"status": "error", "action": "Get Game By Age group", "error_message": str(err)}), 500

    elif "platform" in request.args:
        platform = request.args.get("platform")
        try:
            game = gamesService.get_game_by_platform(platform)
            if game:
                return jsonify({"status": "success", "action": "Get Game By Platform", "game": game})
            else:
                return jsonify({"status": "error", "action": "Get Game By Platform", "error_message": "Game not found"}), 404
        except Exception as err:
            return jsonify({"status": "error", "action": "Get Game By Platform", "error_message": str(err)}), 500

    elif "game_gender" in request.args:
        game_gender = request.args.get("game_gender")
        try:
            game = gamesService.get_game_by_gender(game_gender)
            if game:
                return jsonify({"status": "success", "action": "Get Game By Name", "game": game})
            else:
                return jsonify({"status": "error", "action": "Get Game By Name", "error_message": "Game not found"}), 404
        except Exception as err:
            return jsonify({"status": "error", "action": "Get Game By Name", "error_message": str(err)}), 500

    elif "game_gender" in request.args:
        game_gender = request.args.get("game_gender")
        try:
            game = gamesService.get_game_by_gender(game_gender)
            if game:
                return jsonify({"status": "success", "action": "Get Game By Name", "game": game})
            else:
                return jsonify({"status": "error", "action": "Get Game By Name", "error_message": "Game not found"}), 404
        except Exception as err:
            return jsonify({"status": "error", "action": "Get Game By Name", "error_message": str(err)}), 500

    elif "all" in request.args:
        try:
            games = gamesService.get_all_games()
            return make_response(success_response(action="Get All Games", parameter=games))
        except Exception as err:
            return make_response(error_response(action="Get All Games", error_message=str(err), error_code=500))
    
# Método DELETE para excluir um jogo por ID
@games_bp.route("/<int:game_id>", methods=["DELETE"])
@jwt_required()
def delete_game_by_id(game_id):

    current_user = get_jwt_identity()

    if current_user != "teste@teste.com":
        return make_response(error_response(action="Verification", error_code=403, error_message="User does not have permission"))

    else:
        try:
            deleted_game = gamesService.delete_game_by_id(game_id)
            if deleted_game:
                return jsonify({"status": "success", "action": "Delete Game By ID", "game": deleted_game})
            else:
                return make_response(error_response(action="Delete Game By ID", error_message="Game not found", error_code=404))
        except Exception as err:
            return make_response(error_response(action="Delete Game By ID", error_message=str(err), error_code=500))

@games_bp.route("",methods=["PATCH"])
@jwt_required()
def games_methods():
    
    current_user = get_jwt_identity()

    if current_user != "teste@teste.com":
        return make_response(error_response(action="Verification", error_code=403, error_message="User does not have permission"))

    else:
        if request.method == "PATCH":
            if request.is_json:
                data = request.json
                if len(data) < 1:
                    return make_response(error_response(action="Update Games Info",error_code=400,error_message="missing one or more parameters"))
                elif len(data) > 1:
                    return make_response(error_response(action="Update Games Info",error_code=400,error_message="too many parameters has been passed"))
                elif "gameName" not in data and "price" not in data and "platform" not in data:
                    return make_response(error_response(action="Update Games Info",error_code=400,error_message="error in json format"))
                else:
                    if "gameName" in data:
                        try:
                            gameName = data.get("gameName")
                            current_game = gamesService.get_game_by_name(data.get("gameName"))
                            gamesService.update_gameName(game_id=current_game.id,gameName=gameName)
                            return make_response(success_response(action="Set New Game Name"))
                        except Exception as err:
                            if len(err.args) == 2:
                                return make_response(error_response(action="Set New Game Name",error_message=err.args[0],error_code=err.args[1]))
                            else:
                                return make_response(error_response(action="Set New Game Name",error_message=str(err),error_code=500))

                    elif "secondGameName" in data:
                        try:
                            secondGameName = data.get("secondGameName")
                            current_game = gamesService.get_game_by_second_game_name(data.get("secondGameName"))
                            gamesService.update_second_game_name(game_id=current_game.id,secondGameName=secondGameName)
                            return make_response(success_response(action="Set New Second Game Name"))
                        except Exception as err:
                            if len(err.args) == 2:
                                return make_response(error_response(action="Set Second Game Name",error_message=err.args[0],error_code=err.args[1]))
                            else:
                                return make_response(error_response(action="Set Second Game Name",error_message=str(err),error_code=500))

                    elif "price" in data:
                        try:
                            price = data.get("price")
                            #gamesService.validate_price(price=price)
                            gamesService.update_price(game_id=current_game.id,price=price)
                            return make_response(success_response(action="Set New Price"))
                        except Exception as err:
                            if len(err.args) == 2:
                                return make_response(error_response(action="Set New Price",error_message=err.args[0],error_code=err.args[1]))
                            else:
                                return make_response(error_response(action="Set New Price",error_message=str(err),error_code=500))

                    elif "platform" in data:
                        try:
                            platform = data.get("platform")
                            gamesService.update_platform(game_id=current_game.id,platform=platform)
                            return make_response(success_response(action="Set New platform"))
                        except Exception as err:
                            if len(err.args) == 2:
                                return make_response(error_response(action="Set New platform",error_message=err.args[0],error_code=err.args[1]))
                            else:
                                return make_response(error_response(action="Set New platform",error_message=str(err),error_code=500))
            else:
                return error_response(action="Update Game Info",error_code=400,error_message="Bad Request")