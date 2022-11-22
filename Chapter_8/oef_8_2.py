word = "bananaaaa"
letter = "b"
number = word.count(letter)
print(number)


def counter(x, y):
    count = 0
    for i in x:
        if y == i:
            count += 1
    print(count)


def counter2(x, y):
    return len(x) - len(x.replace(y, ""))


print(counter2(word, letter))
