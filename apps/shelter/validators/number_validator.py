def invalid_number(number: int) -> bool:
    if number < 0 or number > 9999:
        return True
    return False
