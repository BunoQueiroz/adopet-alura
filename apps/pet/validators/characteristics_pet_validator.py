from re import match

def invalid_characteristics_pet(char: str) -> bool:
    pattern = r'^[a-zA-Z\sãôûíéóúáÃÔÛÍÉÓÚÁ]{1,}$'
    return not match(pattern, char)
