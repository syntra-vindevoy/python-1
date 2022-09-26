""" Think Python Chapter 3, Exercise 3.1 (p.26)
jvdoorne, @Home, 26/09/2022
"""


def right_justify(s, col):
    """
    Adds whitespace to the left of a string to justify it to a given column.
    """
    whitespace = ' ' * (col - len(s))
    print(f"{whitespace}{s}")


if __name__ == '__main__':
    # Test
    print("Volgende les:")
    right_justify("Dinsdag 27 september 2022", 32)
