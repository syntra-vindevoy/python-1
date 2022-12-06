"""
2. converteer een int => binary string
geen imports
"""
number = int(input("Give a value to convert to binary number: "))

# number_bin = bin(number)
def int_to_bin(number):
    berekend = number
    result = ""
    while berekend > 0:
        if berekend%2:
            berekend = berekend // 2
            result += "1"
        else:
            berekend = berekend // 2
            result += "O"
    return result[::-1]

number_bin = int_to_bin(number)

print(f"'{number}' converted to binary gives: {number_bin}")
