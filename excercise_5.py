from datetime import datetime
import math

# recursiviteit werkt zeer traag, zie vb eronder = veel sneller
# def fibo(n):
#     if n < 1:
#         return 0
#     if n < 3:
#         return 1
#     return fibo(n-1) + fibo(n-2)


def fibo(n):
    if n < 2:
        return n
    x = 0
    y = 1
    for i in range(2, n+1):
        result = x + y
        x = y
        y = result
    return result


assert 0 == fibo(0), f"fibonacci of 0 expected 0, got: {fibo(0)}"
assert 1 == fibo(1), f"fibonacci of 1 expected 1, got: {fibo(1)}"
assert 1 == fibo(2), f"fibonacci of 2 expected 1, got: {fibo(2)}"
assert 2 == fibo(3), f"fibonacci of 3 expected 2, got: {fibo(3)}"
assert 3 == fibo(4), f"fibonacci of 4 expected 3, got: {fibo(4)}"
assert 5 == fibo(5), f"fibonacci of 5 expected 5, got: {fibo(5)}"
assert 8 == fibo(6), f"fibonacci of 6 expected 8, got: {fibo(6)}"
assert 13 == fibo(7), f"fibonacci of 7 expected 13, got: {fibo(7)}"
print("all tests passed")

if __name__ == "__main__":
    x = 10000
    start = datetime.now()
    for _ in range(1):
        fibo(x)

    end = datetime.now()
    print(end - start)
    print(fibo(x))
    print(len(str(fibo(x))))
    digits = int(math.log10(fibo(x))) + 1
    print(digits)

#
#
# # fac recursive
# def fac(n: int) -> int:
#     if n< 3:
#         return n
#     return n * fac(n - 1)
#
# if __name__ == "__main__":
#     print(fac(10))


# fac recursive
def fac(n: int) -> int:
    for i in range(2, n):
        n *= i
    return n


if __name__ == "__main__":
    start = datetime.now()
    for _ in range(5000000):
        fac(10)

    end = datetime.now()
    print(end - start)
