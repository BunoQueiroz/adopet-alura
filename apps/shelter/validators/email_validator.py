from re import match

def invalid_email(email: str) -> bool:
    pattern = r'^[a-z][a-z0-9]{2,}@[a-z][a-z0-9]{2,}.+[a-z]{0,5}.+[a-z]{0,5}$'
    return not match(pattern, email)
