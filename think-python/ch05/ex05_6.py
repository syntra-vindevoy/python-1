""" Think Python Chapter 5, Exercise 5.6 (p.49)
READ: https://en.wikipedia.org/wiki/Koch_snowflake
jvdoorne, @Syntra, 11/10/2022
"""

import turtle


def koch(t: turtle.Turtle, x, res=4):
    # Base case
    if x < res:
        t.fd(x)
    # Recurse
    else:
        koch(t, x / 3)
        t.lt(60)
        koch(t, x / 3)
        t.rt(120)
        koch(t, x / 3)
        t.lt(60)
        koch(t, x / 3)


def snowflake(t: turtle.Turtle, x):
    for _ in range(3):
        koch(t, x)
        t.rt(120)


if __name__ == '__main__':
    turt_reynolds = turtle.Turtle()
    snowflake(turt_reynolds, 128)
    turtle.mainloop()
