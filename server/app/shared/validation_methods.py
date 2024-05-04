
import re

#TODO: 
def validate_username(username):
    regex = r'^[a-zA-Z0-9_-]{3,16}$'
    pass

def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    pass

def validate_password(password):
    regex = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
    pass

from app.shared.validation_methods import (
    validate_gameName, validate_secondGameName, validate_creator,
    validate_price, validate_year, validate_dlc, validate_gender,
    validate_ageGroup, validate_platform
)

class GameValidation:
    @staticmethod
    def validate_new_game(gameName, secondGameName, creator, price, year, dlc, gender, ageGroup, platform):
        validate_gameName(gameName)
        validate_secondGameName(secondGameName)
        validate_creator(creator)
        validate_price(price)
        validate_year(year)
        validate_dlc(dlc)
        validate_gender(gender)
        validate_ageGroup(ageGroup)
        validate_platform(platform)