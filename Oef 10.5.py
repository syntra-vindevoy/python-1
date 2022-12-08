lst = [1, 2, 3, 4, 5, 5, 7]


def is_sorted():
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    return True
