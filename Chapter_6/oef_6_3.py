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


if __name__ == "__main__":
    print(is_palindrome("redivider"))

