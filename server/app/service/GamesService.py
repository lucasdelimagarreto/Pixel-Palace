from app.shared.validation_methods import GameValidation
from app.model.Games import Games
from app.schemas.GamesSchemas import GamesSchema
from app.repository.GamesRepository import GamesRepository

gamesSchema = GamesSchema()
gamesRepository = GamesRepository()
class GamesService:

    def __init__(self) -> None:
        pass

    def add_new_game(self,gameName,secondGameName,creator,price,year,dlc,gender,ageGroup,platform):        

        games = Games(gameName=None,secondGameName=None,creator=None,price=None,year=None,dlc=None,gender=None,ageGroup=None,platform=None)

        games.gameName = gameName
        games.secondGameName = secondGameName
        games.creator = creator
        games.price = price
        games.year = year
        games.dlc = dlc
        games.gender = gender
        games.ageGroup = ageGroup
        games.platform = platform
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

    def delete_game_by_id(self, game_id):
        # Verifica se o jogo existe antes de tentar excluí-lo
        existing_game = gamesRepository.get_by_id(game_id)
        if existing_game is None:
            raise Exception("Game not found")

        # Chama o método do repositório para excluir o jogo
        deleted_game = gamesRepository.delete_game_by_id(game_id)
        return deleted_game

    def validate_new_game(self, gameName, secondGameName, creator, price, year, dlc, gender, ageGroup, platform):
        GameValidation.validate_new_game(gameName, secondGameName, creator, price, year, dlc, gender, ageGroup, platform)

