from flask import Blueprint,jsonify,request,make_response
from app.repository.GamesRepository import GamesRepository
from app.shared.response import error_response,success_response
from app.service.GamesService import GamesService

games_bp = Blueprint('games_api',__name__,url_prefix='/games')
gamesService = GamesService()

@games_bp.route("",methods=("POST"))
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
def get_game_by_name(game_gender):
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
def get_game_by_name(game_creator):
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
def get_game_by_name(game_year):
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
def get_game_by_name(age_group):
    try:
        game = gamesService.get_game_by_age_group(age_group)
        if game:
            return make_response(success_response(action="Get Game By Age group", parameter=game))
        else:
            return make_response(error_response(action="Get Game By Age group", error_message="Age group not found", error_code=404))
    except Exception as err:
        return make_response(error_response(action="Get Game By Age group", error_message=str(err), error_code=500))

# Método GET para obter um jogo por faixa plataforma
@games_bp.route("/<string:game_platform>", methods=["GET"])
def get_game_by_name(platform):
    try:
        game = gamesService.get_game_by_age_group(platform)
        if game:
            return make_response(success_response(action="Get Game By Platform", parameter=game))
        else:
            return make_response(error_response(action="Get Game By Platform", error_message="Platform not found", error_code=404))
    except Exception as err:
        return make_response(error_response(action="Get Game By Platform", error_message=str(err), error_code=500))
