import re

def different_passwords(password, confirm_password):
    if password != confirm_password:
        return True
    return False

def weak_password(password):
    password = str(password)
    if len(password) >= 8:
        pattern = r'^(?=.*[a-zA-Z])(?=.*\d).+$'
        return not re.match(pattern, password)
    return True
