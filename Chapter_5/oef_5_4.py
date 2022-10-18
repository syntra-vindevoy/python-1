from datetime import datetime

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)


def sum(n):
    for i in range(1, n):
        n += i
    print(n)


if __name__ == "__main__":
    start_1 = datetime.now()
    recurse(5, 10)
    end_1 = datetime.now()
    print(end_1 - start_1)

    start_2 = datetime.now()
    sum(5)
    end_2 = datetime.now()
    print(end_2 - start_2)



