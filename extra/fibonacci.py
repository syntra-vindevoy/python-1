""" Write a function that gives the n-th fibonacci number.
Extra: same, but non-recursively.
jvdoorne, @Syntra, 11/10/2022
"""


def fibo(n):
    # One-liner, couldn't help myself.
    return n if n < 2 else fibo(n - 2) + fibo(n - 1)


def fibo_no_recurse(n):
    if n < 2:
        return n
    else:
        n0, n1 = 0, 1
        for _ in range(n - 1):
            # Yves' solution, via tuple assignment.
            # I used an intermediary variable, c.
            n1, n0 = n1 + n0, n1
        return n1


if __name__ == '__main__':
    for i in range(16):
        print(i, fibo(i), fibo_no_recurse(i))
