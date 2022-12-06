"""Exercise 9.3. Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.
Write a program that prompts the user to enter a string of forbidden letters and then prints the
number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters
that excludes the smallest number of words?
"""
forbidden_letters = input("Give forbidden letters: ")


def avoids(word, forbidden_letters):
    keep = False
    for letter in forbidden_letters:
        if letter in word:
            keep = True
    return keep


with open("words.txt", "r") as input_file:
    lines = input_file.readlines()

for line in lines:
    line = line.strip()
    if avoids(line, forbidden_letters):
        print(line)
