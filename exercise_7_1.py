"""
Exercise 7.1. Copy the loop from Section 7.5 and encapsulate it in a function called mysqrt that
takes a as a parameter, chooses a reasonable value of x, and returns an estimate of the square root of
a.
To test it, write a function named test_square_root that prints a table like this:
a mysqrt(a) math.sqrt(a) diff
- --------- ------------ ----
1.0 1.0 1.0 0.0
2.0 1.41421356237 1.41421356237 2.22044604925e-16
3.0 1.73205080757 1.73205080757 0.0
4.0 2.0 2.0 0.0
5.0 2.2360679775 2.2360679775 0.0
6.0 2.44948974278 2.44948974278 0.0
7.0 2.64575131106 2.64575131106 0.0
8.0 2.82842712475 2.82842712475 4.4408920985e-16
9.0 3.0 3.0 0.0
The first column is a number, a; the second column is the square root of a computed with mysqrt;
the third column is the square root computed by math.sqrt; the fourth column is the absolute value
of the difference between the two estimates
"""
import math

def mysqrt(a, x):
    while True:
        # print(x)
        y = (x + a/x) / 2
        if round(y, 10) == round(x, 10):
            break
        x = y
    return y


def test_square_root():
    print("a", " ", "mysqrt(a)", " ", "math.sqrt(a)", " ", "diff")
    for a in range(1, 10):
        result1 = round(mysqrt(a, a/4), 2)
        result2 = round(math.sqrt(a), 2)
        diff = result1 - result2
        print(f"{a}    {result1:.2f}          {result2:.2f}        {diff:.2f}")


if __name__ == "__main__":
    test_square_root()
