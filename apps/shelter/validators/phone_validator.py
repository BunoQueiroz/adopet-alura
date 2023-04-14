from re import match

def invalid_phone(phone: str) -> bool:
    if phone:
        pattern = r'^(\(?[1-9][1-9]\)?9[1-9]\d{3}-?[1-9]\d{3}|\+55\s\(?[1-9][1-9]\)?9[1-9]\d{3}-?[1-9]\d{3})$'
        return not match(pattern, phone)
    return False
