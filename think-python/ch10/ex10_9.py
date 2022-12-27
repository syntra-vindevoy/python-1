""" Think Python Chapter 10, Exercise 10.9 (p.101)
jvdoorne, @Home, 27/12/2022
"""

from time import perf_counter


def test_add():
    data = []
    with open('../assets/words.txt') as f:
        for line in f.readlines():
            data += [line.strip()]


def test_append():
    data = []
    with open('../assets/words.txt') as f:
        for line in f.readlines():
            data.append(line.strip())


def time_function(func, sample=10):
    t0 = perf_counter()
    for _ in range(sample):
        func()
    return perf_counter() - t0


if __name__ == '__main__':
    n = 16
    print(f"{n}x Add:     {time_function(test_add, n):.2f}s")        # slowest, new list is created
    print(f"{n}x Append:  {time_function(test_append, n):.2f}s")     # fastest, existing list is modified
