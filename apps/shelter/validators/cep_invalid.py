from re import match

def invalid_format_cep(cep: str) -> bool:
    pattern = r'^\d{5}-\d{3}$'
    return not match(pattern, cep)
