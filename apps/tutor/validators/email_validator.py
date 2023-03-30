import re

def email_invalid(email):
    str(email)
    pattern = r'^[a-zA-Z]{1}[\w-]+@[a-zA-Z]+[\w]+.[a-zA-Z]{2,4}.?[a-zA-Z]{0,3}$'
    return not re.match(pattern, email)
