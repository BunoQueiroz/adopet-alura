from re import match

def invalid_state(state: str) -> bool:
    pattern = r'^[A-Z]{2}$'
    return not match(pattern, state)
