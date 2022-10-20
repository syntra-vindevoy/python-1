a = "redivider"
b = "not_a_palindrome"

def first(word):
    return word[0]

def last(word):
        return word[-1]

def middle(word):
        return word[1:-1]

def is_palindrome(word):
    for i in range((int(len(a)))/2):
        word[i] == word[-i]





#print(first(a))
#print(last(a))
#print(middle(a))
print(is_palindrome(a))
