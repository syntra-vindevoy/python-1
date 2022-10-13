from datetime import datetime


def fac(n: int)-> int:
    if n < 3:
        return n

    return n * fac(n- 1)

if __name__ == "__main__":
    start = datetime.now()

    for _ in range(1000):
        fac(10)

        end = datetime.now()

        print(end - start)






