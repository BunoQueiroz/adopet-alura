from re import match

def invalid_size_pet(size: str):
    pattern = r'^(médio|pequeno|grande|Médio|Pequeno|Grande|MÉDIO|PEQUENO|GRANDE|medio|Medio|MEDIO)$'
    return not match(pattern, size)
