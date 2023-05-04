from re import match

def weak_password(password: str) -> bool:
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$'
    return not match(pattern, password)
