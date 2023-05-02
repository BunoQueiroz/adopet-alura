from re import match

def invalid_company_or_user(company_or_user: str) -> bool:
    pattern = r'^(?=.*[a-zA-Z]{3,})[-\w\s]{3,}$'
    return not match(pattern, company_or_user)
