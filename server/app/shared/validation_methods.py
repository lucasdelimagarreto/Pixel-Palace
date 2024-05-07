from datetime import datetime
import re

# Validação de username
def validate_username(username):
    regex = r'^[a-zA-Z0-9_-]{3,16}$'
    if re.match(regex, username):
        return True
    else:
        return False

# Validação de e-mail
def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(regex, email):
        return True
    else:
        return False

# Validação de senha
def validate_password(password):
    regex = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
    if re.match(regex, password):
        return True
    else:
        return False

def validate_age(data_nascimento, idade_minima):
    
    data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d')
    data_atual = datetime.now()
    idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))

    if idade >= idade_minima:
        return True
    else:
        return False

# Validação de nome do jogo
def validate_game_name(game_name):
    # Regra: deve ter pelo menos 3 caracteres
    if len(game_name) >= 3:
        return True
    else:
        return False

# Validação de segundo nome do jogo
def validate_second_game_name(second_game_name):
    # Regra: deve ter pelo menos 1 caractere
    if len(second_game_name) >= 1:
        return True
    else:
        return False
    
# Validação de criador do jogo
def validate_creator(creator):
    # Regra: deve ter pelo menos 1 caractere
    if len(creator) >= 1:
        return True
    else:
        return False

# Validação de preço do jogo
def validate_price(price):
    # Regra: preço deve ser um número positivo
    try:
        price_float = float(price)
        if price_float >= 0:
            return True
        else:
            return False
    except ValueError:
        return False

# Validação de ano do jogo
def validate_year(year):
    # Regra: ano deve ser um número positivo de 4 dígitos
    try:
        year_int = int(year)
        if len(year) == 4 and year_int >= 0:
            return True
        else:
            return False
    except ValueError:
        return False

# Validação de DLC do jogo
def validate_dlc(dlc):
    # Regra: DLC deve ser um booleano
    if isinstance(dlc, bool):
        return True
    else:
        return False

# Validação de genero do jogo
def validate_gender(gender):
    # Regra: deve ter pelo menos 3 caractere
    if len(gender) >= 3:
        return True
    else:
        return False
    
# Validação de ano do jogo
def validate_age_group(ageGroup):
    # Regra: ano deve ser um número positivo de 4 dígitos
    try:
        ageGroup_int = int(ageGroup)
        if len(ageGroup) >= 0 and ageGroup_int >= 0:
            return True
        else:
            return False
    except ValueError:
        return False
    
# Validação de plataforma do jogo
def validate_platform(platform):
    # Regra: deve ter pelo menos 3 caractere
    if len(platform) >= 2:
        return True
    else:
        return False

class GameValidation:
    @staticmethod
    def validate_new_game(gameName, secondGameName, creator, price, year, dlc, gender, ageGroup, platform):
        validate_game_name(gameName)
        validate_second_game_name(secondGameName)
        validate_creator(creator)
        validate_price(price)
        validate_year(year)
        validate_dlc(dlc)
        validate_gender(gender)
        validate_age_group(ageGroup)
        validate_platform(platform)