""" Find various ways to swap the values of two variables x and y
https://betterexplained.com/articles/swap-two-variables-using-xor
jvdoorne, @Syntra, 11/10/2022
"""

if __name__ == '__main__':
    x, y = 5, 12
    print(x, y)

    # Intermediary
    i = x
    x = y
    y = i
    print(x, y)

    # Tuple assignment
    x, y = y, x
    print(x, y)

    # Bitwise XOR
    x = x ^ y
    y = x ^ y
    x = x ^ y
    print(x, y)
