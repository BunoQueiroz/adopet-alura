from re import match

def email_invalid(email: str) -> bool:
    pattern = r'^[a-zA-Z]{1}[\w-]+@[a-zA-Z]+[\w]+.[a-zA-Z]{2,4}.?[a-zA-Z]{0,3}$'
    return not match(pattern, email)
