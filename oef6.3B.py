def first(word):
    """Returns the first character of a string."""
    return word[0]


def last(word):
    """Returns the last of a string."""
    return word[-1]


def middle(word):
    """Returns all but the first and last characters of a string."""
    return word[1:-1]


def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


print(is_palindrome('kak'))
print(is_palindrome('luoool'))
print(is_palindrome('robot'))
print(is_palindrome('kever'))