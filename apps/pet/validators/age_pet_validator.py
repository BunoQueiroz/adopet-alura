from re import match

def invalid_age_pet(age: str) -> bool:
    pattern = r'^\d{1,2}\s[a-zA-Zê]{3,}$'
    return not match(pattern, age)
