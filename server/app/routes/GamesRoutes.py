from flask import Blueprint,jsonify,request,make_response
from app.repository.GamesRepository import GamesRepository
from app.shared.response import error_response,success_response
from app.service.GamesService import GamesService

games_bp = Blueprint('games_api',__name__,url_prefix='/games')
gamesService = GamesService()

@games_bp.route("",methods=("GET", "POST","PUT","DELETE"))
def register():
    
    if request.method == "POST":
        
        if request.is_json:
            
            data = request.get_json()
            
            if len(data) < 3:
                return make_response(error_response(action="Register",error_code=400,error_message="missing one or more parameters"))
            
            elif len(data) > 3:
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
                
                try:
                    gamesService.findGamesByGameName(gameName=gameName)
                
                except:
                    pass
                else:
                    return make_response(error_response(action="Register",error_message="Esse Username já foi cadastrado!",error_code=409))
                
                try:
                    gamesService.findGamesBySecondGameName(secondGameName=secondGameName)
                
                except:
                    pass
                
                else:                   
                    return make_response(error_response(action="Register",error_message="Esse secondGameName já foi cadastrado",error_code=409))
                
                try:
                    gamesService.validate_new_game(gameName,secondGameName,creator,price,year,dlc,gender)
                    response = gamesService.add_new_game(gameName = gameName,secondGameName = secondGameName,creator = creator,price = price,year = year,dlc = dlc,gender = gender)
                    return make_response(success_response(action = "Register",parameter=response))           
                
                except Exception as err:
                    return make_response(error_response(action="Register",error_message=str(err),error_code=409))
                                                        
    return error_response(action="Register",error_code=400,error_message="error")