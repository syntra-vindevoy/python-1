"""
1. converteer een binary string (vb. "110010" ) naar een integer
geen imports
"""

number = input("Give a binary value to convert to int: ")

# number_int = int("0b" + number, 2)
def binary_to_int(number):
    berekend = 1
    for i in number[1:]:
        if i == '0':
            berekend = berekend * 2
        else:
            berekend = berekend * 2 + 1
    return berekend

number_int = binary_to_int(number)


print(f"'{number}' converted to int gives: {number_int}")
