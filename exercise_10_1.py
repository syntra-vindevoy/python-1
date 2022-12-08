"""Exercise 10.1. Write a function called nested_sum that takes a list of lists of integers and adds up
the elements from all of the nested lists. For example:
t = [[1, 2], [3], [4, 5, 6]]
nested_sum(t)
"""


def nested_sum(lst):
    total = 0
    for x in lst:
        if type(x) == list:
            for y in x:
                total += y
        else:
            total += x
    return total


t = [[1, 2], [3], [4, 5, 6]]

result = nested_sum(t)
print(result)