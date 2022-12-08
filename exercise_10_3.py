"""
Exercise 10.3. Write a function called middle that takes a list and returns a new list that contains
all but the first and last elements. For example:
t = [1, 2, 3, 4]
middle(t)
[2, 3]
"""


def middle(lst):
    return lst[1:-1]


t = [1, 2, 3, 4]
result = middle(t)
print(result)