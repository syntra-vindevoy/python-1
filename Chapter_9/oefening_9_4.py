def uses_only(a: str, b: str):
    for letter in a:
        if letter not in b:
            return False
    return True

