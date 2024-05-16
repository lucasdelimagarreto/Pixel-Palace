from app.shared.validation_methods import GameValidation
from app.model.Games import Games
from app.schemas.GamesSchemas import GamesSchema
from app.repository.GamesRepository import GamesRepository

gamesSchema = GamesSchema()
gamesRepository = GamesRepository()
class GamesService:

    def __init__(self) -> None:
        pass

    def add_new_game(self,gameName,secondGameName,creator,price,year,dlc,gender,ageGroup,platform,description):        

        games = Games(gameName=None,secondGameName=None,creator=None,price=None,year=None,dlc=None,gender=None,ageGroup=None,platform=None, description=None)

        games.gameName = gameName
        games.secondGameName = secondGameName
        games.creator = creator
        games.price = price
        games.year = year
        games.dlc = dlc
        games.gender = gender
        games.ageGroup = ageGroup
        games.platform = platform
        games.description = description
        gamesRepository.save(games)
        return gamesSchema.dump(games)

    def get_all_games(self):
        return gamesRepository.get_all_games()

    def get_game_by_id(self, game_id):
        return gamesRepository.get_by_id(game_id)

    def get_game_by_name(self, game_name):
        return gamesRepository.get_by_name(game_name)

    def get_game_by_second_game_name(self,secondGameName):
        games = gamesRepository.get_by_second_game_name(secondGameName=secondGameName)
        return games

    def get_game_by_creator(self, creator):
        games = gamesRepository.get_by_creator(creator=creator)
        return games

    def get_game_by_year(self, year):
        games = gamesRepository.get_by_year(year=year)
        return games

    def get_game_by_gender(self, gender):
        games = gamesRepository.get_by_gender(gender=gender)
        return games

    def get_game_by_age_group(self, ageGroup):
        games = gamesRepository.get_by_age_group(ageGroup=ageGroup)
        return games

    def get_game_by_platform(self, platform):
        games = gamesRepository.get_by_platform(platform=platform)
        return games

    def update_gameName(self,game_id,gameName):
        game = gamesRepository.get_by_id(game_id)
        game.gameName = gameName
        gamesRepository.update(game)
        return

    def update_second_game_name(self,game_id,secondGameName):
        game = gamesRepository.get_by_id(game_id)
        game.secondGameName = secondGameName
        gamesRepository.update(game)
        return

    def update_creator(self,game_id,creator):
        game = gamesRepository.get_by_id(game_id)
        game.creator = creator
        gamesRepository.update(game)
        return

    def update_price(self,game_id,price):
        game = gamesRepository.get_by_id(game_id)
        game.price = price
        gamesRepository.update(game)
        return
    
    def update_platform(self,game_id,platform):
        game = gamesRepository.get_by_id(game_id)
        game.platform = platform
        gamesRepository.update(game)
        return
    
    def update_description(self,game_id,description):
        game = gamesRepository.get_by_id(game_id)
        game.description = description
        gamesRepository.update(game)
        return

    def delete_game_by_id(self, game_id):

        existing_game = gamesRepository.get_by_id(game_id)
        if existing_game is None:
            raise Exception("Game not found")

        deleted_game = gamesRepository.delete_game_by_id(game_id)
        return deleted_game

    def save_game(self, game):
        gamesRepository.update(game)
        return
    
    def validate_new_game(self, gameName, secondGameName, creator, price, year, dlc, gender, ageGroup, platform, description):
        GameValidation.validate_new_game(gameName, secondGameName, creator, price, year, dlc, gender, ageGroup, platform, description)