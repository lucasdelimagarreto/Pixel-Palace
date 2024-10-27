from app.shared.dataBase import db

user_games = db.Table(

    "user_games",
    db.Model.metadata,
    db.Column('games_id', db.ForeignKey("games.id"),primary_key=True),
    db.Column('user_id', db.ForeignKey("users.id"),primary_key=True)

)