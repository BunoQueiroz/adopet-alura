from re import match

def invalid_number(number: str) -> bool:
    if number:
        pattern = r'^\d{1,4}$'
        return not match(pattern, number)
    return False
