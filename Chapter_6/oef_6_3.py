def first(word):
    return word[0]


def last(word):
    return word[-1]
    # return word[len(word)-1]


def middle(word):
    return word[1: -1]


def is_palindrome(word):
    if len(word) == 1:
        return True
    if len(word) == 2:
        return first(word) == last(word)
    if first(word) == last(word):
        return is_palindrome(middle(word))
    else:
        return False


def is_palindrome_easy(word):
    return word == word[::-1]


if __name__ == "__main__":
    assert is_palindrome_easy("bob")
    assert not is_palindrome_easy("ward")
    assert is_palindrome("bob")
    assert not is_palindrome("ward")

