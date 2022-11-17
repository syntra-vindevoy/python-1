"""
Exercise 8.2. There is a string method called count that is similar to the function in Section 8.7.
Read the documentation of this method and write an invocation that counts the number of a’s in
'banana'.
"""
text = "banana"
letter = "a"

aantal = text.count(letter)
print(aantal)


aantal = len(text) - len(text.replace(letter,""))
print(aantal)
