"""
Exercise 10.5. Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise. For example:
is_sorted([1, 2, 2])
True
is_sorted(['b', 'a'])
False
"""


def is_sorted(lst):
    ascending = True
    previous = lst[0]
    for x in range(1, len(lst)):
        if lst[x] >= previous:
            previous = lst[x]
            continue
        else:
            ascending = False
            break
    return ascending


def is_sorted2(lst):
    for i in range(1,len(lst)):
        if lst[i] < lst[i-1]:
            return False
    return True


result1 = is_sorted([1, 2, 2])
result2 = is_sorted(['b', 'a'])

print(result1, " ", result2)
