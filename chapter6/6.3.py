

def is_palindrome(string):

    def first(word):
        return word[0]

    def last(word):
        return word[-1]

    def middle(word):
        return word[1:-1]

    if len(string) > 2:
        if first(string) == last(string):
            return is_palindrome(middle(string))
        else:
            return False

    else:
        return True


print(is_palindrome("redivider"))
