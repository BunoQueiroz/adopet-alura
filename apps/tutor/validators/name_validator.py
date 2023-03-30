import re

def full_name_invalid(name):
    name = str(name)
    pattern = r'^[a-zA-Zç~^áéíóúãõâô]{2,}\s.*[a-zA-Zç~^áéíóúãõâô]{4,}.*'
    return not bool(re.match(pattern, name))
