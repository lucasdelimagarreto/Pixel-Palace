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

                required_params = ["gameName", "secondGameName", "creator", "price", "year", "dlc", "gender", "ageGroup", "platform", "description", "publisher", "imageBanner", "videoPromotional"]
                if not all(param in data for param in required_params):
                    return make_response(error_response(action="Register", error_code=400, error_message="One or more parameters are missing"))

                try:
                    gamesService.get_game_by_name(gameName=data["gameName"])
                except:
                    pass
                else:
                    return make_response(error_response(action="Register", error_message="This game has already been registered!", error_code=409))

                try:
                    gamesService.validate_new_game(
                        data["gameName"], data["secondGameName"], data["creator"], data["price"], data["year"], data["dlc"], data["gender"], 
                        data["ageGroup"], data["platform"], data["description"], data["publisher"], data["imageBanner"], data["videoPromotional"]
                    )
                    response = gamesService.add_new_game(
                        gameName=data["gameName"], secondGameName=data["secondGameName"], creator=data["creator"], price=data["price"], year=data["year"], 
                        dlc=data["dlc"], gender=data["gender"], ageGroup=data["ageGroup"], platform=data["platform"], description=data["description"], 
                        publisher=data["publisher"], imageBanner=data["imageBanner"], videoPromotional=data["videoPromotional"]
                    )
                    return make_response(success_response(action="Register", parameter=response))
                except Exception as err:
                    return make_response(error_response(action="Register", error_message=str(err), error_code=410))

    return error_response(action="Register", error_code=400, error_message="Error")

# Métodos GET para obter um jogo
@games_bp.route("/filter", methods=["GET"])
def get_game():

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
            games = gamesService.get_game_by_name(game_name)
            if games:
                return jsonify({"status": "success", "action": "Get Game By Name", "games": games})
            else:
                return jsonify({"status": "error", "action": "Get Game By Name", "error_message": "Games not found"}), 404
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

    elif "publisher" in request.args:
        publisher = request.args.get("publisher")
        try:
            game = gamesService.get_game_by_publisher(publisher)
            if game:
                return jsonify({"status": "success", "action": "Get Game By publisher", "game": game})
            else:
                return jsonify({"status": "error", "action": "Get Game By publisher", "error_message": "Game not found"}), 404
        except Exception as err:
            return jsonify({"status": "error", "action": "Get Game By publisher", "error_message": str(err)}), 500
    
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

@games_bp.route("/change", methods=["PATCH"])
@jwt_required()
def change_games():
    current_user = get_jwt_identity()
    data = request.json

    if current_user != "teste@teste.com":
        return make_response(error_response(action="Verification", error_code=403, error_message="User does not have permission"))

    if not request.is_json:
        return make_response(error_response(action="Update Game Info", error_code=400, error_message="Bad Request"))

    if not data:
        return make_response(error_response(action="Update Games Info", error_code=400, error_message="Missing parameters"))

    allowed_fields = {"id", "newGameName", "newSecondGameName", "newPrice", "newPlatform", "newCreator", "newPublisher", "newYear", "newDlc", "newGender", "newAgeGroup", "newDescription", "newImageBanner", "newVideoPromotional"}
    invalid_fields = set(data.keys()) - allowed_fields

    if invalid_fields:
        return make_response(error_response(action="Update Games Info", error_code=400, error_message="Invalid parameters provided"))

    if "id" not in data:
        return make_response(error_response(action="Update Games Info", error_code=400, error_message="Primary identifier 'id' missing"))

    try:
        current_game = gamesService.get_game_by_id(data["id"])
        if not current_game:
            return make_response(error_response(action="Update Games Info", error_code=404, error_message="Game not found"))

        if "newGameName" in data:
            current_game.gameName = data["newGameName"]
            gamesService.update_game_name(current_game.id, current_game.gameName)
        if "newSecondGameName" in data:
            current_game.secondGameName = data["newSecondGameName"]
            gamesService.update_second_game_name(current_game.id, current_game.secondGameName)
        if "newPrice" in data:
            current_game.price = data["newPrice"]
            gamesService.update_price(current_game.id, current_game.price)
        if "newPlatform" in data:
            current_game.platform = data["newPlatform"]
            gamesService.update_platform(current_game.id, current_game.platform)
        if "newCreator" in data:
            current_game.creator = data["newCreator"]
            gamesService.update_creator(current_game.id, current_game.creator)
        if "newPublisher" in data:
            current_game.publisher = data["newPublisher"]
            gamesService.update_publisher(current_game.id, current_game.publisher)
        if "newYear" in data:
            current_game.year = data["newYear"]
            gamesService.update_year(current_game.id, current_game.year)
        if "newDlc" in data:
            current_game.dlc = data["newDlc"]
            gamesService.update_dlc(current_game.id, current_game.dlc)
        if "newGender" in data:
            current_game.gender = data["newGender"]
            gamesService.update_gender(current_game.id, current_game.gender)
        if "newAgeGroup" in data:
            current_game.ageGroup = data["newAgeGroup"]
            gamesService.update_ageGroup(current_game.id, current_game.ageGroup)
        if "newDescription" in data:
            current_game.description = data["newDescription"]
            gamesService.update_description(current_game.id, current_game.description)
        if "newImageBanner" in data:
            current_game.imageBanner = data["newImageBanner"]
            gamesService.update_imageBanner(current_game.id, current_game.imageBanner)
        if "newVideoPromotional" in data:
            current_game.videoPromotional = data["newVideoPromotional"]
            gamesService.update_videoPromotional(current_game.id, current_game.videoPromotional)

        return make_response(success_response(action="Update Game Info"))

    except Exception as err:
        if len(err.args) == 2:
            return make_response(error_response(action="Update Game Info", error_message=err.args[0], error_code=err.args[1]))
        else:
            return make_response(error_response(action="Update Game Info", error_message=str(err), error_code=500))
        
@games_bp.route("/all", methods=["GET"])
def get_all_games():
    try:
        games = gamesService.get_all_games()
        games_dict = [game.to_dict() for game in games]
        return make_response(success_response(action="Get All Games", parameter=games_dict))
    except Exception as err:
        return make_response(error_response(action="Get All Games", error_message=str(err), error_code=500))
