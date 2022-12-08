lst_1 = [[5, 2], [9], [6, 5, 6]]
lst_2 = []


def nested_sum():
    for i in lst_1:
        lst_2.extend(i)
    print(lst_2)


nested_sum()
