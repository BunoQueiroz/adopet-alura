from re import match

def invalid_borhood(borhood: str) -> bool:
    if borhood:
        pattern = r'^[a-zA-Z\s]{3,}$'
        return not match(pattern, borhood)
    return False
