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
"""
@games_bp.route("/filter", methods=["GET"])
def get_game():

    if "game_id" in request.args:
        game_id = request.args.get("game_id")
        try:
            game = gamesService.get_game_by_id(game_id)
            
            return jsonify({"status": "success", "action": "Get Game By Id", "game": game})
        except Exception as err:
            return jsonify({"status": "error", "action": "Get Game By Id", "error_message": str(err)}), 500

    elif "game_name" in request.args:
        game_name = request.args.get("game_name")
        try:
            game = gamesService.get_game_by_name(game_name)
            if game:
                game = games_schema.dump(game)
                return jsonify({"status": "success", "action": "Get Game By Name", "games": game})
            else:
                return jsonify({"status": "error", "action": "Get Game By Name", "error_message": "Games not found"}), 404
        except Exception as err:
            return jsonify({"status": "error", "action": "Get Game By Name", "error_message": str(err)}), 500

    elif "game_gender" in request.args:
        game_gender = request.args.get("game_gender")
        try:
            game = gamesService.get_game_by_gender(game_gender)
            if game:
                game = games_schema.dump(game)
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
                game = games_schema.dump(game)
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
                game = games_schema.dump(game)
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
                game = games_schema.dump(game)
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
                game = games_schema.dump(game)
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
                game = games_schema.dump(game)
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
                game = games_schema.dump(game)
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
                game = games_schema.dump(game)
                return jsonify({"status": "success", "action": "Get Game By Name", "game": game})
            else:
                return jsonify({"status": "error", "action": "Get Game By Name", "error_message": "Game not found"}), 404
        except Exception as err:
            return jsonify({"status": "error", "action": "Get Game By Name", "error_message": str(err)}), 500
"""
@games_bp.route("/filter", methods=["GET"])
def get_game():
    """
    Retrieves games based on query parameters.

    Handles requests for games by ID, name, genre, creator, year, age group,
    platform, or publisher. Returns success or error responses with detailed
    messages.
    """

    search_params = {}  # Dictionary to store search criteria

    # Extract query parameters efficiently using a loop
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

    # Validate query parameters (optional for added security)
    # ... (implement validation logic here)

    try:
        # Delegate game retrieval to a dedicated function for clarity
        game = get_game_by_criteria(search_params)

        if game:
            game = games_schema.dump(game)
            return jsonify(
                {"status": "success", "action": get_action_text(search_params), "game": game}
            )
        else:
            return jsonify(
                {
                    "status": "error",
                    "action": get_action_text(search_params),
                    "error_message": "Game not found",
                }
            ), 404

    except Exception as err:
        return jsonify(
            {"status": "error", "action": get_action_text(search_params), "error_message": str(err)}
        ), 500

def get_game_by_criteria(search_params):
    """
    Retrieves a game based on the provided search criteria.

    This function simplifies code by handling the logic for retrieving games
    based on different parameters.
    """

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
        # Use the appropriate lookup function based on search parameters
        lookup_param = next(iter(search_params))  # Get first parameter
        lookup_function = game_lookup_method[lookup_param]
        return lookup_function(search_params[lookup_param])

    except (KeyError, StopIteration) as e:
        # Handle invalid or missing search parameters
        return None

def get_action_text(search_params):
    """
    Constructs a human-readable action text based on search parameters.

    This function improves code readability by extracting the action text
    from the search parameters.
    """

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
    else:
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
        else:
            return jsonify({"status": "error", "message": "No games found matching the search term"}), 404

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500