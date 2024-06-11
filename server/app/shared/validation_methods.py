from datetime import datetime
import re

# Validação de username
def validate_username(username):
    regex = r'^[a-zA-Z0-9_-]{3,16}$'
    return bool(re.match(regex, username))

# Validação de e-mail
def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return bool(re.match(regex, email))

# Validação de senha
def validate_password(password):
    regex = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
    return bool(re.match(regex, password))

# Validação de idade
def validate_age(data_nascimento, idade_minima):
    data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d')
    data_atual = datetime.now()
    idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))
    return idade >= idade_minima

# Validação de nome do jogo
def validate_game_name(game_name):
    return len(game_name) >= 3

# Validação de segundo nome do jogo
def validate_second_game_name(second_game_name):
    return len(second_game_name) >= 1

# Validação de criador do jogo
def validate_creator(creator):
    return len(creator) >= 1

# Validação de publisher do jogo
def validate_publisher(publisher):
    return len(publisher) >= 1

# Validação de preço do jogo
def validate_price(price):
    try:
        return float(price) >= 0
    except ValueError:
        return False

# Validação de ano do jogo
def validate_year(year):
    return isinstance(year, int) and year >= 0

# Validação de DLC do jogo
def validate_dlc(dlc):
    return isinstance(dlc, bool)

# Validação de genero do jogo
def validate_gender(gender):
    return len(gender) >= 3

# Validação de grupo de idade do jogo
def validate_age_group(ageGroup):
    return isinstance(ageGroup, int) and ageGroup >= 0

# Validação de plataforma do jogo
def validate_platform(platform):
    return len(platform) >= 2

# Validação de descrição do jogo
def validate_description(description):
    return len(description) >= 3

# Validação de imagem do banner
def validate_imageBanner(imageBanner):
    return isinstance(imageBanner, str) and imageBanner.lower().endswith('.jpg')

# Validação de vídeo promocional
def validate_videoPromotional(videoPromotional):
    youtube_regex = re.compile(r'^(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+$')
    return bool(youtube_regex.match(videoPromotional))

class GameValidation:
    @staticmethod
    def validate_new_game(gameName, secondGameName, creator, publisher, price, year, dlc, gender, ageGroup, platform, description, imageBanner, videoPromotional):
        if not validate_game_name(gameName):
            raise ValueError("Invalid game name")
        if not validate_second_game_name(secondGameName):
            raise ValueError("Invalid second game name")
        if not validate_creator(creator):
            raise ValueError("Invalid creator name")
        if not validate_publisher(publisher):
            raise ValueError("Invalid publisher name")
        if not validate_price(price):
            raise ValueError("Invalid price")
        if not validate_year(year):
            raise ValueError("Invalid year")
        if not validate_dlc(dlc):
            raise ValueError("Invalid DLC value")
        if not validate_gender(gender):
            raise ValueError("Invalid gender")
        if not validate_age_group(ageGroup):
            raise ValueError("Invalid age group")
        if not validate_platform(platform):
            raise ValueError("Invalid platform")
        if not validate_description(description):
            raise ValueError("Invalid description")
        if not validate_imageBanner(imageBanner):
            raise ValueError("Invalid image banner")
        if not validate_videoPromotional(videoPromotional):
            raise ValueError("Invalid video promotional link")
        return True