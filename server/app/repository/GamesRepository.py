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
        # Para mais de 1 objeto Json result = schema.dump(game,many=True)
        try:
            game = db.session.scalars(db.select(Games).filter_by(gameName=game_name)).all()
            result = schema.dump(game,many=True)
            if not game:
                raise Exception(f"No game found with name '{game_name}'")
            return result
        except Exception as e:
            raise e

    def get_by_gender(self, gender):
        try:
            game = db.session.scalars(db.select(Games).filter_by(gender=gender)).all()
            result = schema.dump(game,many=True)
            if not game:
                raise Exception(f"No game found with name '{gender}'")
            return result
        except Exception as e:
            raise e

    def get_by_id(self, game_id):
        try:
            game = db.session.scalars(db.select(Games).filter_by(id=game_id)).first()
            if not game:
                raise Exception(f"No game found with ID '{game_id}'")
            return game
        except Exception as e:
            raise e

    def get_by_second_game_name(self, second_game_name):
        try:
            game = db.session.scalars(db.select(Games).filter_by(secondGameName=second_game_name)).all()
            result = schema.dump(game,many=True)
            if not game:
                raise Exception(f"No game found with name '{second_game_name}'")
            return result
        except Exception as e:
            raise e

    def get_by_creator(self, creator):
        try:
            game = db.session.scalars(db.select(Games).filter_by(creator=creator)).all()
            result = schema.dump(game,many=True)
            if not game:
                raise Exception(f"No game found with name '{creator}'")
            return result
        except Exception as e:
            raise e
        
    def get_by_publisher(self, publisher):
        try:
            game = db.session.scalars(db.select(Games).filter_by(publisher=publisher)).all()
            result = schema.dump(game,many=True)
            if not game:
                raise Exception(f"No game found with name '{publisher}'")
            return result
        except Exception as e:
            raise e

    def get_by_year(self, year):
        try:
            game = db.session.scalars(db.select(Games).filter_by(year=year)).all()
            result = schema.dump(game,many=True)
            if not game:
                raise Exception(f"No game found with name '{year}'")
            return result
        except Exception as e:
            raise e

    def get_by_age_group(self, age_group):
        try:
            game = db.session.scalars(db.select(Games).filter_by(ageGroup=age_group)).all()
            result = schema.dump(game,many=True)
            if not game:
                raise Exception(f"No game found with name '{age_group}'")
            return result
        except Exception as e:
            raise e

    def get_by_platform(self, platform):
        try:
            game = db.session.scalars(db.select(Games).filter_by(platform=platform)).all()
            result = schema.dump(game,many=True)
            if not game:
                raise Exception(f"No game found with name '{platform}'")
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