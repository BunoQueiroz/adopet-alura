from re import match

def invalid_email(email: str) -> bool:
    if email:
        pattern = r'^[a-z]+[a-z0-9\-]+@[a-z][a-z0-9\-]+.[a-z]{2,5}.{,1}[a-z]{,4}$'
        return not match(pattern, email)
    return True
