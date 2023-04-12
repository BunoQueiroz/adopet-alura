from re import match

def invalid_name_pet(name: str) -> bool:
    pattern = r'^[a-zA-Z\sõãçóíúéáêôÕÃÓÍÚÉÁÊÔ]{2,}$'
    return not match(pattern, name)
