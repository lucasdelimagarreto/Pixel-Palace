from app.shared.validation_methods import GameValidation
from app.model.Games import Games
from app.schemas.GamesSchemas import GamesSchema
from app.repository.GamesRepository import GamesRepository

gamesSchema = GamesSchema()
gamesRepository = GamesRepository()
class GamesService:

    def __init__(self) -> None:
        pass

    def add_new_game(self,gameName,secondGameName,creator, publisher,price,year,dlc,
                     gender,ageGroup,platform,description,imageBanner,videoPromotional):        

        games = Games(gameName=None,secondGameName=None,creator=None,publisher=None,price=None,year=None,dlc=None,
                      gender=None,ageGroup=None,platform=None, description=None,imageBanner=None,videoPromotional=None)

        games.gameName = gameName
        games.secondGameName = secondGameName
        games.creator = creator
        games.publisher = publisher
        games.price = price
        games.year = year
        games.dlc = dlc
        games.gender = gender
        games.ageGroup = ageGroup
        games.platform = platform
        games.description = description
        games.imageBanner = imageBanner
        games.videoPromotional = videoPromotional
        gamesRepository.save(games)
        return gamesSchema.dump(games)

    def serialize_game(self, game):
        return {
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
            "videoPromotional": game.videvideoPromotionaloPromocional
        }
    
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
    
    def get_game_by_publisher(self, publisher):
        games = gamesRepository.get_by_publisher(publisher=publisher)
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

    # ----------------------------------------------------------------------- #
    
    def update_game_name(self,game_id,newgameName):
        game = gamesRepository.get_by_id_scalar(game_id)
        if game == None:             
            raise Exception("Games not exists")
        game.gameName = newgameName
        gamesRepository.update(game)
        return

    def update_second_game_name(self,game_id,secondGameName):
        game = gamesRepository.get_by_id_scalar(game_id)
        if game == None:             
            raise Exception("Games not exists")
        game.secondGameName = secondGameName
        gamesRepository.update(game)
        return

    def update_creator(self,game_id,creator):
        game = gamesRepository.get_by_id_scalar(game_id)
        if game == None:             
            raise Exception("Games not exists")
        game.creator = creator
        gamesRepository.update(game)
        return
    
    def update_publisher(self,game_id,publisher):
        game = gamesRepository.get_by_id_scalar(game_id)
        if game == None:             
            raise Exception("Games not exists")
        game.publisher = publisher
        gamesRepository.update(game)
        return

    def update_price(self,game_id,price):
        game = gamesRepository.get_by_id_scalar(game_id)
        if game == None:             
            raise Exception("Games not exists")
        game.price = price
        gamesRepository.update(game)
        return
    
    def update_platform(self,game_id,platform):
        game = gamesRepository.get_by_id_scalar(game_id)
        if game == None:             
            raise Exception("Games not exists")
        game.platform = platform
        gamesRepository.update(game)
        return
    
    def update_description(self,game_id,description):
        game = gamesRepository.get_by_id_scalar(game_id)
        if game == None:             
            raise Exception("Games not exists")
        game.description = description
        gamesRepository.update(game)
        return
    
    def update_year(self,game_id,year):
        game = gamesRepository.get_by_id_scalar(game_id)
        if game == None:             
            raise Exception("Games not exists")
        game.year = year
        gamesRepository.update(game)
        return
    
    def update_dlc(self,game_id,dlc):
        game = gamesRepository.get_by_id_scalar(game_id)
        if game == None:             
            raise Exception("Games not exists")
        game.dlc = dlc
        gamesRepository.update(game)
        return
    
    def update_gender(self,game_id,gender):
        game = gamesRepository.get_by_id_scalar(game_id)
        if game == None:             
            raise Exception("Games not exists")
        game.gender = gender
        gamesRepository.update(game)
        return
    
    def update_ageGroup(self,game_id,ageGroup):
        game = gamesRepository.get_by_id_scalar(game_id)
        if game == None:             
            raise Exception("Games not exists")
        game.ageGroup = ageGroup
        gamesRepository.update(game)
        return
    
    def update_imageBanner(self,game_id,imageBanner):
        game = gamesRepository.get_by_id_scalar(game_id)
        if game == None:             
            raise Exception("Games not exists")
        game.imageBanner = imageBanner
        gamesRepository.update(game)
        return

    def update_videoPromotional(self,game_id,videoPromotional):
        game = gamesRepository.get_by_id_scalar(game_id)
        if game == None:             
            raise Exception("Games not exists")
        game.videoPromotional = videoPromotional
        gamesRepository.update(game)
        return
    
    # ----------------------------------------------------------------------- #
    
    def delete_game_by_id(self, game_id):
        game = gamesRepository.get_by_id_scalar(game_id)
        if game == None:             
            raise Exception("Games not exists")
        gamesRepository.delete(game)
        return
        

    def save_game(self, game):
        gamesRepository.update(game)
        return
    
    def validate_new_game(self, gameName, secondGameName, creator, publisher, price, year, dlc, gender, ageGroup, platform, description, imageBanner, videoPromotional):
        GameValidation.validate_new_game(gameName, secondGameName, creator, publisher, price, year, dlc, gender, ageGroup, platform, description, imageBanner, videoPromotional)