import math

def is_power(a, b):
    y = math.log(a, b)
    return (b ** y) == a

print(is_power(9, 3))
print(is_power(12, 2))

