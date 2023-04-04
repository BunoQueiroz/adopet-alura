from re import match

def full_name_invalid(name: str) -> bool:
    pattern = r'^[a-zA-Zç~^áéíóúãõâô]{2,}\s.*[a-zA-Zç~^áéíóúãõâô]{4,}+$'
    return not match(pattern, name)
