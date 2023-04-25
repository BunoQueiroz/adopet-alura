from re import match

def invalid_password(password: str) -> bool:
    pattern = r'^(?=.*[a-zA-Z])(?=.*[\d])[-.,;:_=+@#$%&*!a-zA-Z\d]{8,}$' # Para conter pelo menos um caracter especial -> (?=.*[.,;:-_=+@#$%&*!])
    return not match(pattern, password)

#!@-+