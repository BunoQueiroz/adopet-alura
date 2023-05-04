from re import match

def invalid_email(email: str) -> bool:
    pattern = r'^[a-z][-_.a-z0-9]{2,}@[a-z][-a-z0-9]{2,}\.{1}[a-z]{2,5}\.{0,1}[a-z]{0,5}$'
    return not match(pattern, email)
