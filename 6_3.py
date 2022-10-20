# def first(word):
#     return word[0]
#
#
# def last(word):
#     return word[-1]
#
#
# def middle(word):
#     return word[1:-1]
#
#
# def is_palindrome(word):
#     if len(word) <= 1:
#         return True
#     if first(word) != last(word):
#         return False
#     return is_palindrome(middle(word))
#
#
# print(is_palindrome("lepel"))


def is_palindrome():
    s = input("what word?")

    if s.lower().split() == s.lower().split()[::-1]:
        print("true")
    else:
        print("false")



is_palindrome()




