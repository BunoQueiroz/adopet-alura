from re import match

def invalid_name_road(road: str) -> bool:
    if road:
        pattern = r'^[a-zA-Z0-9çãàáíîóôú\s_-]{4,}$'
        return not match(pattern, road)
    return False
