from re import match

def full_name_invalid(name: str) -> bool:
    pattern = r'^[a-zA-Zçáéíóúãõâô]{2,}\s[\sa-zA-Zçáéíóúãõâô]{4,}+$'
    return not match(pattern, name)
