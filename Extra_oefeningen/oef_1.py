# converteer binaire string naar integer


def convert_to_integer(a: str):
    sum = 0
    for digit in a:
        sum = sum * 2 + int(digit)

    return sum


#prompt = input("Please enter binary string")
#print(convert_to_integer(prompt))


def convert_to_integer_bis(b: str):
    sum = 0
    j = 0
    for i in b[::-1]:
        sum += int(i) * (2 ** j)
        j += 1
    return sum


# prompt_2 = input("Please enter binary string")
# print(convert_to_integer_bis(prompt_2))

if __name__ == "__main__":
    assert convert_to_integer_bis("1010") == 10
    assert convert_to_integer("1010") == 10
    assert convert_to_integer_bis("110010") == 50
    assert convert_to_integer("110010") == 50
