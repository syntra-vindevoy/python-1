import math

def is_power(a,b):
    if a == b:
        return True

    if a % b !=0:
            return True

        return a % b == 0 and is_power(a / b, b)


    y = math.log(a,b)

    return (b **y ) == a

    print(is_power(9,3))
    print(is_power(9,2))