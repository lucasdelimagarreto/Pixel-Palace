from app.model.Games import Games
from app.shared.baseRepository import BaseRepository
from app.shared.dataBase import db
from app.schemas.GamesSchemas import GamesSchema

schema = GamesSchema()

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
            games = db.session.query(Games).filter_by(gameName=game_name).all()
            if not games:
                raise Exception(f"No game found with name '{game_name}'")
            result = schema.dump(games, many=True)
            return result
        except Exception as e:
            raise e

    def get_by_gender(self, gender):
        try:
            games = db.session.query(Games).filter_by(gender=gender).all()
            if not games:
                raise Exception(f"No game found with gender '{gender}'")
            result = schema.dump(games, many=True)
            return result
        except Exception as e:
            raise e

    def get_by_id(self, game_id):
        try:
            game = db.session.query(Games).filter_by(id=game_id).first()
            if not game:
                raise Exception(f"No game found with ID '{game_id}'")
            result = schema.dump(game)
            return result
        except Exception as e:
            raise e

    def get_by_second_game_name(self, second_game_name):
        try:
            games = db.session.query(Games).filter_by(secondGameName=second_game_name).all()
            if not games:
                raise Exception(f"No game found with second game name '{second_game_name}'")
            result = schema.dump(games, many=True)
            return result
        except Exception as e:
            raise e

    def get_by_creator(self, creator):
        try:
            games = db.session.query(Games).filter_by(creator=creator).all()
            if not games:
                raise Exception(f"No game found with creator '{creator}'")
            result = schema.dump(games, many=True)
            return result
        except Exception as e:
            raise e

    def get_by_publisher(self, publisher):
        try:
            games = db.session.query(Games).filter_by(publisher=publisher).all()
            if not games:
                raise Exception(f"No game found with publisher '{publisher}'")
            result = schema.dump(games, many=True)
            return result
        except Exception as e:
            raise e

    def get_by_year(self, year):
        try:
            games = db.session.query(Games).filter_by(year=year).all()
            if not games:
                raise Exception(f"No game found with year '{year}'")
            result = schema.dump(games, many=True)
            return result
        except Exception as e:
            raise e

    def get_by_age_group(self, age_group):
        try:
            games = db.session.query(Games).filter_by(ageGroup=age_group).all()
            if not games:
                raise Exception(f"No game found with age group '{age_group}'")
            result = schema.dump(games, many=True)
            return result
        except Exception as e:
            raise e

    def get_by_platform(self, platform):
        try:
            games = db.session.query(Games).filter_by(platform=platform).all()
            if not games:
                raise Exception(f"No game found with platform '{platform}'")
            result = schema.dump(games, many=True)
            return result
        except Exception as e:
            raise e

    def delete_game_by_id(self, game_id):
        try:
            game_to_delete = self.get_by_id(game_id)
            if game_to_delete:
                db.session.delete(game_to_delete)
                db.session.commit()
                return game_to_delete
            else:
                return None
        except Exception as e:
            raise e