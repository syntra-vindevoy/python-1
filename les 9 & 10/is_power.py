def is_power(a, b):
    if a < b:
        return False
    if a % b == 0:
        return is_power(a/b, b) or a/b == 1
