from flask import Blueprint,jsonify,request,make_response
from app.shared.validation_methods import GameValidation
from app.repository.GamesRepository import GamesRepository
from app.shared.baseRepository import BaseRepository
from app.shared.response import error_response,success_response
from app.service.GamesService import GamesService

games_bp = Blueprint('games_api',__name__,url_prefix='/games')
gamesService = GamesService()

@games_bp.route("",methods=["POST"])
def register():

    if request.method == "POST":

        if request.is_json:

            data = request.get_json()

            if len(data) < 8:
                return make_response(error_response(action="Register",error_code=400,error_message="missing one or more parameters"))

            elif len(data) > 8:
                return make_response(error_response(action="Register",error_code=400,error_message="too many parameters has been passed"))

            elif "gameName" not in data or "secondGameName" not in data or "creator" not in data or "price" not in data or "year" not in data or "dlc" not in data or "gender" not in data:
                return make_response(error_response(action="Register",error_code=400,error_message="error in json format"))

            else:
                gameName = data.get("gameName")
                secondGameName = data.get("secondGameName")
                creator = data.get("creator")
                price = data.get("price")
                year = data.get("year")
                dlc = data.get("dlc")
                gender = data.get("gender")
                ageGroup = data.get("ageGroup")

                try:
                    gamesService.get_game_by_name(gameName=gameName)

                except:
                    pass
                else:
                    return make_response(error_response(action="Register",error_message="Esse Game já foi cadastrado!",error_code=409))

                try:
                    gamesService.validate_new_game(gameName,secondGameName,creator,price,year,dlc,gender,ageGroup)
                    response = gamesService.add_new_game(gameName = gameName,secondGameName = secondGameName,creator = creator,price = price,year = year,dlc = dlc,gender = gender,ageGroup = ageGroup)
                    return make_response(success_response(action = "Register",parameter=response))           

                except Exception as err:
                    return make_response(error_response(action="Register",error_message=str(err),error_code=409))

    return error_response(action="Register",error_code=400,error_message="error")

# Método GET para obter todos os jogos
@games_bp.route("", methods=["GET"])
def get_all_games():
    try:
        games = gamesService.get_all_games()
        return make_response(success_response(action="Get All Games", parameter=games))
    except Exception as err:
        return make_response(error_response(action="Get All Games", error_message=str(err), error_code=500))

# Método GET para obter um jogo por ID
@games_bp.route("/<int:game_id>", methods=["GET"])
def get_game_by_id(game_id):
    try:
        game = gamesService.get_game_by_id(game_id)
        if game:
            return make_response(success_response(action="Get Game By ID", parameter=game))
        else:
            return make_response(error_response(action="Get Game By ID", error_message="Game not found", error_code=404))
    except Exception as err:
        return make_response(error_response(action="Get Game By ID", error_message=str(err), error_code=500))

# Método GET para obter um jogo por nome
@games_bp.route("/<string:game_name>", methods=["GET"])
def get_game_by_name(game_name):
    try:
        game = gamesService.get_game_by_name(game_name)
        if game:
            return make_response(success_response(action="Get Game By Name", parameter=game))
        else:
            return make_response(error_response(action="Get Game By Name", error_message="Game not found", error_code=404))
    except Exception as err:
        return make_response(error_response(action="Get Game By Name", error_message=str(err), error_code=500))
    
# Método GET para obter um jogo por genero
@games_bp.route("/<string:game_gender>", methods=["GET"])
def get_game_by_gender(game_gender):
    try:
        game = gamesService.get_game_by_gender(game_gender)
        if game:
            return make_response(success_response(action="Get Game By Gender", parameter=game))
        else:
            return make_response(error_response(action="Get Game By Gender", error_message="Gender not found", error_code=404))
    except Exception as err:
        return make_response(error_response(action="Get Game By Gender", error_message=str(err), error_code=500))

# Método GET para obter um jogo por criador
@games_bp.route("/<string:game_creator>", methods=["GET"])
def get_game_by_creator(game_creator):
    try:
        game = gamesService.get_game_by_creator(game_creator)
        if game:
            return make_response(success_response(action="Get Game By Creator", parameter=game))
        else:
            return make_response(error_response(action="Get Game By Creator", error_message="Creator not found", error_code=404))
    except Exception as err:
        return make_response(error_response(action="Get Game By Creator", error_message=str(err), error_code=500))

# Método GET para obter um jogo por ano
@games_bp.route("/<string:game_year>", methods=["GET"])
def get_game_by_year(game_year):
    try:
        game = gamesService.get_game_by_year(game_year)
        if game:
            return make_response(success_response(action="Get Game By Year", parameter=game))
        else:
            return make_response(error_response(action="Get Game By Year", error_message="Any game of this Year", error_code=404))
    except Exception as err:
        return make_response(error_response(action="Get Game By Year", error_message=str(err), error_code=500))

# Método GET para obter um jogo por faixa etária
@games_bp.route("/<string:game_age_group>", methods=["GET"])
def get_game_by_age_group(age_group):
    try:
        game = gamesService.get_game_by_age_group(age_group)
        if game:
            return make_response(success_response(action="Get Game By Age group", parameter=game))
        else:
            return make_response(error_response(action="Get Game By Age group", error_message="Age group not found", error_code=404))
    except Exception as err:
        return make_response(error_response(action="Get Game By Age group", error_message=str(err), error_code=500))

# Método GET para obter um jogo por plataforma
@games_bp.route("/<string:game_platform>", methods=["GET"])
def get_game_by_platform(platform):
    try:
        game = gamesService.get_game_by_platform(platform)
        if game:
            return make_response(success_response(action="Get Game By Platform", parameter=game))
        else:
            return make_response(error_response(action="Get Game By Platform", error_message="Platform not found", error_code=404))
    except Exception as err:
        return make_response(error_response(action="Get Game By Platform", error_message=str(err), error_code=500))

# Método DELETE para excluir um jogo por ID
@games_bp.route("/<int:game_id>", methods=["DELETE"])
def delete_game_by_id(game_id):
    try:
        deleted_game = gamesService.delete_game_by_id(game_id)
        if deleted_game:
            return make_response(success_response(action="Delete Game By ID", parameter=deleted_game))
        else:
            return make_response(error_response(action="Delete Game By ID", error_message="Game not found", error_code=404))
    except Exception as err:
        return make_response(error_response(action="Delete Game By ID", error_message=str(err), error_code=500))


'''
@games_bp.route("/games/<int:game_id>", methods=["PUT"])
def edit_game(game_id):
    try:
        if not request.is_json:
            return make_response(error_response(action="EditarJogo", error_code=400, error_message="O corpo da solicitação deve estar em formato JSON"))

        data = request.get_json()
        if not data:
            return make_response(error_response(action="EditarJogo", error_code=400, error_message="Dados de jogo ausentes"))

        game = gamesService.get_game_by_id(game_id)
        if not game:
            return make_response(error_response(action="EditarJogo", error_code=404, error_message="Jogo não encontrado"))

        # Atualiza as características do jogo com base nos dados recebidos
        if "title" in data:
            game.gameName = data["title"]
        if "genre" in data:
            game.gender = data["genre"]
        if "price" in data:
            game.price = data["price"]
        if "description" in data:
            game.description = data["description"]
        
        gamesService.save_game(game)

        return make_response(success_response(action="EditarJogo", message="Jogo atualizado com sucesso"))

    except Exception as err:
        return make_response(error_response(action="EditarJogo", error_code=500, error_message=str(err)))'''

@games_bp.route("",methods=["PATCH"])

def games_methods(current_game):
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
                        gamesService.validate_price(price=price)
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