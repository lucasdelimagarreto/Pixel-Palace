from app.model.Games import Games
from app.shared.baseRepository import BaseRepository
from app.shared.dataBase import db

class GamesRepository(BaseRepository):

    def __init__(self):
        super().__init__(Games)

    def get_all_games(self):
        try:
            games = db.session.query(Games).all()
            return games
        except Exception as e:
            raise e

    def get_by_name(self, game_name):
        try:
            game = db.session.query(Games).filter_by(gameName=game_name).first()
            if not game:
                raise Exception(f"No game found with name '{game_name}'")
            return game
        except Exception as e:
            raise e

    def get_by_gender(self, gender):
        try:
            game = db.session.query(Games).filter_by(gender=gender).first()
            if not game:
                raise Exception(f"No game found with gender '{gender}'")
            return game
        except Exception as e:
            raise e

    def get_by_id(self, game_id):
        try:
            game = db.session.query(Games).filter_by(id=game_id).first()
            if not game:
                raise Exception(f"No game found with ID '{game_id}'")
            return game
        except Exception as e:
            raise e

    def get_by_second_game_name(self, second_game_name):
        try:
            game = db.session.query(Games).filter_by(secondGameName=second_game_name).first()
            if not game:
                raise Exception(f"No game found with second game name '{second_game_name}'")
            return game
        except Exception as e:
            raise e

    def get_by_creator(self, creator):
        try:
            game = db.session.query(Games).filter_by(creator=creator).first()
            if not game:
                raise Exception(f"No game found with creator '{creator}'")
            return game
        except Exception as e:
            raise e

    def get_by_year(self, year):
        try:
            game = db.session.query(Games).filter_by(year=year).first()
            if not game:
                raise Exception(f"No game found with year '{year}'")
            return game
        except Exception as e:
            raise e

    def get_by_age_group(self, age_group):
        try:
            game = db.session.query(Games).filter_by(ageGroup=age_group).first()
            if not game:
                raise Exception(f"No game found with age group '{age_group}'")
            return game
        except Exception as e:
            raise e

    def get_by_platform(self, platform):
        try:
            game = db.session.query(Games).filter_by(platform=platform).first()
            if not game:
                raise Exception(f"No game found with platform '{platform}'")
            return game
        except Exception as e:
            raise e

    def delete_game_by_id(self, game_id):
        try:
            game = self.get_by_id(game_id)
            if game:
                super().delete(game)
                return game
            else:
                raise Exception(f"No game found with ID '{game_id}'")
        except Exception as e:
            raise e