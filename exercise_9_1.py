"""Exercise 9.1. Write a program that reads words.txt and prints only the words with more than 20
characters (not counting whitespace).
"""

with open("words.txt", "r") as input_file:
    lines = input_file.readlines()

for line in lines:
    line = line.strip()
    if len(line) > 20:
        print(line)
