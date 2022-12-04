def to_int(binary: str):
    value = 1

    for digit in binary[1:]:
        value *= 2

        if digit == "1":
            value += 1

    return value


def to_binary(number: int):
    binary = ""

    while number > 0:
        number, remainder = divmod(number, 2)
        binary = remainder + binary

    return binary


def main():
    assert to_int("11") == 3
    assert to_int("100") == 4
    assert to_int("110010") == 50

    assert to_binary(3) == "11"
    assert to_binary(4) == "100"
    assert to_binary(50) == "110010"


if __name__ == "__main__":
    main()
