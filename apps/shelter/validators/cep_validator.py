from re import match

def invalid_format_cep(cep: str) -> bool:
    if cep:
        pattern = r'^\d{5}-\d{3}$'
        return not match(pattern, cep)
    return False
