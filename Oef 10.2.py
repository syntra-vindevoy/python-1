lst_1 = [1, 2, 3]


def cumulative(m):
    cumulative_sum = 0
    new_list = []
    for i in m:
        cumulative_sum += i
        new_list.append(cumulative_sum)
    print(new_list)


cumulative(lst_1)
