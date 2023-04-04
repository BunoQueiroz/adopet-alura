from re import match

def different_passwords(password: str, confirm_password: str) -> bool:
    if password != confirm_password:
        return True
    return False

def weak_password(password: str) -> bool:
    if len(password) >= 8:
        pattern = r'^(?=.*[a-zA-Z])(?=.*\d).+$'
        return not match(pattern, password)
    return True
