def fibo(n: int):
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)


def fibo_non_rec(n: int):
    if n < 2:
        return n
    a = 0
    b = 1
    c = int()
    for _ in range(n):
        c = b + a
        a, b = b, c
    return c


if __name__ == "__main__":
    for i in range(500):
        print(fibo_non_rec(i))
