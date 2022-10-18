""" Think Python Chapter 6, Exercise 6.3 (p.61)
jvdoorne, @Syntra, 18/10/2022
"""


def is_palindrome(s):
    # Sorry, hahahaha
    return s == s[::-1]


def is_palindrome_bis(s):
    # For real now, recursively
    if len(s) <= 1:
        return True
    if len(s) == 2:
        return s[0] == s[-1]
    return s[0] == s[-1] and is_palindrome_bis(s[1:-1])


if __name__ == '__main__':
    print(is_palindrome_bis("noon"))
    print(is_palindrome_bis("redivider"))
    print(is_palindrome_bis("palindrome"))
