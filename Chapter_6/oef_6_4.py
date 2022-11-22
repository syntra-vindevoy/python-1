def is_power(a, b):
    if a % b != 0:
        return False
    if a == b:
        return True
    else:
        return is_power(a / b, b)


def is_power_bis(a, b):
    if a % b == 0:
        return is_power_bis(a / b, b) or a == b


def is_power_bisbis(a, b):
    if a == b:
        return True
    return a % b == 0 and is_power_bis(a / b, b)


if __name__ == "__main__":
    print(is_power(9, 3))
    print(is_power_bis(9, 3))
