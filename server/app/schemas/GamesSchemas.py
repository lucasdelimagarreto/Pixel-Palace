from app.model.Games import Games
from app.shared.dataBase import marshmallow as ma

class GamesSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Games

    id = ma.auto_field()
    gameName = ma.auto_field()
    secondGameName = ma.auto_field()
    creator = ma.auto_field()
    price = ma.auto_field()
    year = ma.auto_field()
    dlc = ma.auto_field()
    gender = ma.auto_field()
    ageGroup = ma.auto_field()
    platform = ma.auto_field()
    description = ma.auto_field()