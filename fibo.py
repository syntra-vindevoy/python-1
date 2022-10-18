from datetime import datetime
from math import log10, floor

from numpy import log


def fibo(n):
    if n < 2:
        return n

    n_min_2 = 0
    n_min_1 = 1

    for i in range(n - 1):
        n_min_1, n_min_2 = n_min_1 + n_min_2, n_min_1
        #sum = n_min_2 + n_min_1
        #n_min_2 = n_min_1
        #n_min_1 = sum

    return n_min_1


if __name__ == "__main__":
    #for i in range(5, 501, 5):
    #    start = datetime.now()
    #    print(fibo(i))
    #    end = datetime.now()
    #    print(end - start)

    #for i in range(11):
    #    print(fibo(i))

    r = fibo(500)
    print(r)
    print(floor(log10(r)) + 1)
