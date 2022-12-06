"""
find number van 1 tem 10000
terugmelden wat juiste nummer was en in hoeveel stappen dit gevonden is
"""
import random
import datetime as dt

random.seed
min = 1
max = 100001
number = random.randint(min, max - 1)


def find_number(n, min, max):
    search_min = min
    search_max = max
    i = 1
    search_value = min + (max - min) / 2
    while n != search_value:
        if n > search_value:
            search_min = search_value
            search_value = search_min + (search_max - search_min) // 2
            i += 1
        else:
            search_max = search_value
            search_value = search_min + (search_max - search_min) // 2
            i += 1

    # print(f'Getal was: {search_value}, gevonden in {i} stappen')
    return int(search_value), i


# assert find_number(1, 1, 10001) == (1, 14)
# assert find_number(2, 1, 10001) == (2, 13)
# assert find_number(5000, 1, 10001) == (5000, 14)
# assert find_number(5002, 1, 10001) == (5002, 13)
# assert find_number(9999, 1, 10001) == (9999, 13)
# assert find_number(10000, 1, 10001) == (10000, 14)
start = dt.datetime.now()
for i in range( min, max):
    find_number(i, min, max)
end = dt.datetime.now()
print(end - start)
# if __name__ == "__main__":
#     find_number(number, min, max)
