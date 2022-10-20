"""
Exercise 6.2. The Ackermann function, A(m, n), is defined:
A(m, n) =



n + 1 if m = 0
A(m − 1, 1) if m > 0 and n = 0
A(m − 1, A(m, n − 1)) if m > 0 and n > 0.
See http: // en. wikipedia. org/ wiki/ Ackermann_ function . Write a function named ack
that evaluates the Ackermann function. Use your function to evaluate ack(3, 4), which should be
125. What happens for larger values of m and n? Solution: http: // thinkpython2. com/ code/
ackermann. py .
"""


def ack(m, n):
    if m == 0:
        n = n + 1

    if m > 0 and n == 0:
        ack(m - 1, 1)

    if m > 0 and n > 0:
        ack(m - 1, ack(m, n - 1))


if __name__ == "__main__":
    assert ack(3, 4) == 125
