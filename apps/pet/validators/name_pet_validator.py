from re import match

def invalid_pet_name(name: str) -> bool:
    pattern = r'^[a-zA-Z\sõãçóíúéáêôÕÃÓÍÚÉÁÊÔ]{2,}$'
    return not match(pattern, name)
