from re import match

def invalid_name_city(city: str) -> bool:
    pattern = r'^[a-zA-Z_\s-]{4,}$'
    return not match(pattern, city)
