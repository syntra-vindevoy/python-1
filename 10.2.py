def cumsum(a):
    cumulative_sum = 0
    total = 0
    cumsum_list = []
    for i in a:
        total += i
        cumsum_list.append(total)
    print(cumsum_list)
cumsum(range(1,11))
