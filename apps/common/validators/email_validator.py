from re import match
from tutor.models import Tutor


def invalid_email(email: str) -> bool:
    if Tutor.objects.filter(email=email).exists():
        return True
    pattern = r'^[a-z][-_.a-z0-9]{2,}@[a-z][-a-z0-9]{2,}\.{1}[a-z]{2,5}\.{0,1}[a-z]{0,5}$'
    return not match(pattern, email)
