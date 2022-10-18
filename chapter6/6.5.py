def gcd(a, b):
    if b != 0:
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)
    else:
        return 1


print(gcd(42, 8))
