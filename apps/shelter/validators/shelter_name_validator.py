from re import match

def invalid_name_shelter(name: str) -> bool:
    pattern = r'^(?=.*[a-zA-Z]).+$'
    return not match(pattern, name)
