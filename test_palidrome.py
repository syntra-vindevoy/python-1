def palindrome_varia(word2):
    a =word2
    b = word2[::-1]
    if a == b:
        print("right, this is a palindrome")
    else:
        print("omg...this is not a palindrome")

palindrome_varia("allen")
palindrome_varia("bob")
palindrome_varia("otto")
palindrome_varia("redivider")