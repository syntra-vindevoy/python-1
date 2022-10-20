"""
Exercise 6.4. A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
function called is_power that takes parameters a and b and returns True if a is a power of b. Note:
you will have to think about the base case.
"""


def is_power(a, b):
    if a == 1:
        return b == 1

    test = 1
    while test < a:
        test = test * b
    return test == a


def is_power2(a, b):
    if a % b == 0:
        return is_power2(a / b, b) or (a / b == 1)


def is_power3(a, b):
    y = math.log(a, b)
    return b ** y == a


if __name__ == "__main__":
    # automatisch testen functie is_power
    number_1 = 0
    number_2 = 2
    test = is_power(number_1, number_2)
    assert test is False, f"Checking if {number_1} is a power of {number_2}, expected False, got: {test}"
    number_1 = 1
    number_2 = 2
    test = is_power(number_1, number_2)
    assert test is False, f"Checking if {number_1} is a power of {number_2}, expected False, got: {test}"
    number_1 = 2
    number_2 = 2
    test = is_power(number_1, number_2)
    assert test is True, f"Checking if {number_1} is a power of {number_2}, expected True, got: {test}"
    number_1 = 3
    number_2 = 2
    test = is_power(number_1, number_2)
    assert test is False, f"Checking if {number_1} is a power of {number_2}, expected False, got: {test}"
    number_1 = 4
    number_2 = 2
    test = is_power(number_1, number_2)
    assert test is True, f"Checking if {number_1} is a power of {number_2}, expected True, got: {test}"
    number_1 = 5
    number_2 = 2
    test = is_power(number_1, number_2)
    assert test is False, f"Checking if {number_1} is a power of {number_2}, expected False, got: {test}"
