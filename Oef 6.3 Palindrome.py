a = "redivider"
b = "not_a_palindrome"

def first(word):
    return word[0]

def last(word):
        return word[-1]

def middle(word):
        return word[1:-1]

def length(word):

    for i in range(int(len(word) / 2)):
        return word[0:i-1]
     #   i = i-1

print(length(a))
"""
def test(word):
    return (int(len(word) / 2))


print(test(a))


#def is_palindrome(word):
#    for i in range((int(len(a)))/2):
#         if word[i] == word[-i]:

        #for i in range((int(len(a)))/2):
         #   word[i] == word[-i]

 #   else:
#      print("not a palindrome")

#def test():
#    for i in range[0:((int(len(a)))/2):]:
      #      word[i] == word[-i]

#print(test(a))
#print(first(a))
#print(last(a))
#print(middle(a))
#print(is_palindrome(a))

"""