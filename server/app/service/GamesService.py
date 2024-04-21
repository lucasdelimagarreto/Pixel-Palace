from app.shared.validation_methods import validate_creator, validate_dlc, validate_gameName, validate_gender, validate_price, validate_secondGameName, validate_username,validate_email,validate_password, validate_year
from app.model.Games import Games
from app.schemas.GamesSchemas import GamesSchema
from app.repository.GamesRepository import GamesRepository

games = Games(gameName=None,secondGameName=None,creator=None,price=None,year=None,dlc=None,gender=None)
gamesSchema = GamesSchema()
gamesRepository = GamesRepository()
class GamesService:
    
    def __init__(self) -> None:
        pass

    def add_new_game(self,gameName,secondGameName,creator,price,year,dlc,gender):        

        games.gameName = gameName
        games.secondGameName = secondGameName
        games.creator = creator
        games.price = price
        games.year = year
        games.dlc = dlc
        games.gender = gender
        gamesRepository.save(games)
        return gamesSchema.dump(games)
    
    def findGamesById(self,id):
        games = gamesRepository.getById(id=id)
        return games
    
    def findGamesByGameName(self,gameName):
        games = gamesRepository.getByGamename(gameName=gameName)
        return games
    
    def findGamesBySecondGameName(self,secondGameName):
        games = gamesRepository.getBySecondGameName(secondGameName=secondGameName)
        return games

    def findGamesByCreator(self, creator):
        games = gamesRepository.getByCreator(creator=creator)
        return games
    
    def findGamesByYear(self, year):
        games = gamesRepository.getByYear(year=year)
        return games
    
    def findGamesByGender(self, gender):
        games = gamesRepository.getByGender(gender=gender)
        return games
    
    def validate_new_game(self,gameName,secondGameName,creator,price,year,dlc,gender):
        validate_gameName(gameName)
        validate_secondGameName(secondGameName)
        validate_creator(creator)
        validate_price(price)
        validate_year(year)
        validate_dlc(dlc)
        validate_gender(gender)
        pass