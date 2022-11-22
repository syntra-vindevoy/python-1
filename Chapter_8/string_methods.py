name = "ward"
print(name.startswith("wa"))


word = "banana"
index = 0
while index < len(word):
    letter = word[len(word)-1 -index]
    print(letter)
    index += 1


prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == "O" or letter == "Q":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)

x = "yves"
print(x[0:2:-1])
