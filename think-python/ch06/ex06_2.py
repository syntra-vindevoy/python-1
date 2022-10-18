""" Think Python Chapter 6, Exercise 6.2 (p.61)
jvdoorne, @Syntra, 18/10/2022
"""


def ack(m, n):
    # Expect RecursionErrors with large inputs
    # https://en.wikipedia.org/wiki/Ackermann_function
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m - 1, 1)
    return ack(m - 1, ack(m, n - 1))


if __name__ == '__main__':
    print(ack(3, 4))
