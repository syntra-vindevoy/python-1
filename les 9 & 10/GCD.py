def gcd(a, b):
    """Gives the greatest common divisor"""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
