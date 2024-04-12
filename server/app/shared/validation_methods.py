
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
