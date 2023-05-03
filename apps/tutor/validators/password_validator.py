from re import match

def weak_password(password: str) -> bool:
    pattern = r'^(?=.*[a-zA-Z])(?=.*\d).{8,}$'
    return not match(pattern, password)
