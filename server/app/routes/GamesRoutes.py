from flask import Blueprint,jsonify,request,make_response
from app.shared.response import error_response,success_response
from app.service.GamesService import GamesService
from app.schemas.GamesSchemas import GamesSchema
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.model.Games import Games

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
                    gamesService.validate_new_game(**data)
                    response = gamesService.add_new_game(**data)
                    return make_response(success_response(action="Register", parameter=response))
                except Exception as err:
                    return make_response(error_response(action="Register", error_message=str(err), error_code=410))

    return error_response(action="Register", error_code=400, error_message="Error")

game_schema = GamesSchema()
games_schema = GamesSchema(many=True)

# Métodos GET para obter um jogo
@games_bp.route("/filter", methods=["GET"])
def get_game():

    search_params = {}

    for param in request.args:
        if param in [
            "game_id",
            "game_name",
            "game_gender",
            "game_creator",
            "game_year",
            "age_group",
            "platform",
            "publisher",
        ]:
            search_params[param] = request.args.get(param)

    try:
        # Busca o jogo com base nos parâmetros
        game = get_game_by_criteria(search_params)

        if game:
            # Serializa o resultado corretamente
            serialized_game = game_schema.dump(game)

            # Verifique se a serialização foi bem-sucedida
            if not serialized_game or serialized_game == [{}]:
                return jsonify({"status": "error", "action": get_action_text(search_params), "error_message": "No valid game data found"}), 404

            return jsonify({"status": "success", "action": get_action_text(search_params), "game": serialized_game})
        return jsonify({"status": "error", "action": get_action_text(search_params), "error_message": "Game not found"}), 404

    except Exception as err:
        return jsonify({"status": "error", "action": get_action_text(search_params), "error_message": str(err)}), 500

def get_game_by_criteria(search_params):
    """
    Retrieves a game based on the provided search criteria.

    This function simplifies code by handling the logic for retrieving games
    based on different parameters.
    """

    # Dicionário de funções mapeadas para cada critério
    game_lookup_method = {
        "game_id": gamesService.get_game_by_id,
        "game_name": gamesService.get_game_by_name,
        "game_gender": gamesService.get_game_by_gender,
        "game_creator": gamesService.get_game_by_creator,
        "game_year": gamesService.get_game_by_year,
        "age_group": gamesService.get_game_by_age_group,
        "platform": gamesService.get_game_by_platform,
        "publisher": gamesService.get_game_by_publisher,
    }

    try:
        # Use a função de lookup correta com base nos parâmetros de busca
        lookup_param = next(iter(search_params))  # Obtém o primeiro parâmetro
        lookup_function = game_lookup_method.get(lookup_param)
        # Verifique se a função de busca existe
        if lookup_function:
            return lookup_function(search_params[lookup_param])
        else:
            raise ValueError(f"Invalid search parameter: {lookup_param}")

    except (KeyError, StopIteration, ValueError) as e:
        # Lida com parâmetros de busca inválidos ou ausentes
        return None


def get_action_text(search_params):

    action_map = {
        "game_id": "Get Game By Id",
        "game_name": "Get Game By Name",
        "game_gender": "Get Game By Genre",
        "game_creator": "Get Game By Creator",
        "game_year": "Get Game By Year",
        "age_group": "Get Game By Age group",
        "platform": "Get Game By Platform",
        "publisher": "Get Game By publisher",
    }

    lookup_param = next(iter(search_params))  # Get first parameter
    return action_map.get(lookup_param, "Unknown Action")  # Handle missing keys

# Método DELETE para excluir um jogo por ID
@games_bp.route("/<int:game_id>", methods=["DELETE"])
@jwt_required()
def delete_game_by_id(game_id):

    current_user = get_jwt_identity()

    if current_user != "teste@teste.com":
        return make_response(error_response(action="Verification", error_code=403, error_message="User does not have permission"))
    try:
        gamesService.delete_game_by_id(game_id)
            
        return make_response(success_response(action="Delete"))

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

    allowed_fields = {
        "id", "newGameName", "newSecondGameName", "newPrice", "newPlatform",
        "newCreator", "newPublisher", "newYear", "newDlc", "newGender",
        "newAgeGroup", "newDescription", "newImageBanner", "newVideoPromotional"
    }
    invalid_fields = set(data.keys()) - allowed_fields

    if invalid_fields:
        return make_response(error_response(action="Update Games Info", error_code=400, error_message="Invalid parameters provided"))

    if "id" not in data:
        return make_response(error_response(action="Update Games Info", error_code=400, error_message="Primary identifier 'id' missing"))

    try:
        if "newGameName" in data:
            gamesService.update_game_name(data["id"], data["newGameName"])
        if "newSecondGameName" in data:
            gamesService.update_second_game_name(data["id"], data["newSecondGameName"])
        if "newPrice" in data:
            gamesService.update_price(data["id"], data["newPrice"])
        if "newPlatform" in data:
            gamesService.update_platform(data["id"], data["newPlatform"])
        if "newCreator" in data:
            gamesService.update_creator(data["id"], data["newCreator"])
        if "newPublisher" in data:
            gamesService.update_publisher(data["id"], data["newPublisher"])
        if "newYear" in data:
            gamesService.update_year(data["id"], data["newYear"])
        if "newDlc" in data:
            gamesService.update_dlc(data["id"], data["newDlc"])
        if "newGender" in data:
            gamesService.update_gender(data["id"], data["newGender"])
        if "newAgeGroup" in data:
            gamesService.update_ageGroup(data["id"], data["newAgeGroup"])
        if "newDescription" in data:
            gamesService.update_description(data["id"], data["newDescription"])
        if "newImageBanner" in data:
            gamesService.update_imageBanner(data["id"], data["newImageBanner"])
        if "newVideoPromotional" in data:
            gamesService.update_videoPromotional(data["id"], data["newVideoPromotional"])

        return make_response(success_response(action="Update Game Info"))

    except Exception as err:
        if len(err.args) == 2:
            return make_response(error_response(action="Update Game Info", error_message=err.args[0], error_code=err.args[1]))
        return make_response(error_response(action="Update Game Info", error_message=str(err), error_code=500))

@games_bp.route("/all", methods=["GET"])
def get_all_games():
    try:
        games = gamesService.get_all_games()
        games_dict = [game.to_dict() for game in games]
        return make_response(success_response(action="Get All Games", parameter=games_dict))
    except Exception as err:
        return make_response(error_response(action="Get All Games", error_message=str(err), error_code=500))

@games_bp.route("/search", methods=["GET"])
def search_games():
    search_term = request.args.get("search_term")
    
    if not search_term or search_term.strip() == "":
        return jsonify({"error": "Invalid search_term parameter"}), 400
    if not search_term:
        return jsonify({"error": "Missing search_term parameter"}), 400

    try:
        games = Games.query.filter(
            (Games.gameName.ilike(f"%{search_term}%")) |
            (Games.secondGameName.ilike(f"%{search_term}%")) |
            (Games.gender.ilike(f"%{search_term}%")) |
            (Games.platform.ilike(f"%{search_term}%"))  
        ).all()

        if games:
            games_data = [{
                "id": game.id,
                "gameName": game.gameName,
                "secondGameName": game.secondGameName,
                "creator": game.creator,
                "price": game.price,
                "year": game.year,
                "dlc": game.dlc,
                "gender": game.gender,
                "ageGroup": game.ageGroup,
                "platform": game.platform,
                "description": game.description,
                "publisher": game.publisher,
                "imageBanner": game.imageBanner,
                "videoPromotional": game.videoPromotional
            } for game in games]

            return jsonify({"status": "success", "games": games_data})
        return jsonify({"status": "error", "message": "No games found matching the search term"}), 404

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500