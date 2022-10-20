"""
Exercise 3.3. Note: This exercise should be done using only the statements and other features we
have learned so far.
1. Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
Hint: to print more than one value on a line, you can print a comma-separated sequence of
values:
print('+', '-')
By default, print advances to the next line, but you can override that behavior and put a
space at the end, like this:
print('+', end=' ')
print('-')
"""

def print_lijntype_1():
    print("+", "-"*4, "+", "-"*4, "+")

def print_lijntype_2():
    print("/", " " * 4, "/", " " * 4, "/")

print_lijntype_1()
i = 1
while i <= 4:
    print_lijntype_2()
    i += 1
print_lijntype_1()
i = 1
while i <= 4:
    print_lijntype_2()
    i += 1
print_lijntype_1()
