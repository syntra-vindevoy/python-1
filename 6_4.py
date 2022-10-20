import math

def is_power(a, b):

    if a == b:
        return True
    if a % b != 0:
        return False
    return is_power(a / b, b)

print(is_power(9, 3))
print(is_power(9, 2))









