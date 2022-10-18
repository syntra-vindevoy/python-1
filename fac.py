from datetime import datetime


def fac(n: int) -> int:
    if n < 3:
        return n

    return n * fac(n - 1)

def fac_loop(n:int) -> int:
    for i in range (2, n):
        n *=i

    return n


if __name__ == "__main__":
    start = datetime.now()

    for _ in range(5000000):
        _ = fac(10)

    end = datetime.now()

    start_2 = datetime.now()

    for _ in range(5000000):
        _ = fac_loop(10)

    end_2 = datetime.now()



    print(end - start)
    print(fac_loop(10))
    print(end_2 - start_2)
    print(fac_loop(10))
