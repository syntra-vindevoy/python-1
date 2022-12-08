"""Exercise 10.2. Write a function called cumsum that takes a list of numbers and returns the cumulative sum;
 that is, a new list where the ith element is the sum of the first i + 1 elements from the
original list. For example:
t = [1, 2, 3]
cumsum(t)
[1, 3, 6]
"""


def cumsum(lst):
    totals = [lst[0]]
    for x in range(1, len(lst)):
        totals.append(totals[x-1] + lst[x])
    return totals


t = [1, 2, 3]
result = cumsum(t)
print(result)
