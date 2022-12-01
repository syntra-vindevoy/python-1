binary = input("Enter a binary number:")


def binarybodecimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    print("The decimal value is:", decimal)


if __name__ == "__main__":
    binarybodecimal(binary)
