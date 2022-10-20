def is_power(a, b):
    if a % b != 0:
        return False

    if a == b:
        return True
    else:
        return is_power(a / b, b)


if __name__ == "__main__":
    print(is_power(78, 3))
