from re import match

def invalid_password(password: str) -> bool:
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[\d])[\w@#!*.,<>;:=+-]{8,}$'
    return not match(pattern, password)
