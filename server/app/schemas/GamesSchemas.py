from app.model.Games import Games
from app.shared.dataBase import marshmallow as ma

class GamesSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Games

    id = ma.auto_field()
    username = ma.auto_field()
    email = ma.auto_field()
    password = ma.auto_field()