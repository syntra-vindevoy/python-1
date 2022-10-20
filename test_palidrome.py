def palindrome_varia(word2):
    a =word2
    b = word2[::-1]
    if a == b:
        print("is a palindrome")
    else:
        print("is not a palindrome")

print(palindrome_varia("allen"))
print(palindrome_varia('bob'))
print(palindrome_varia('otto'))
print(palindrome_varia('redivider'))