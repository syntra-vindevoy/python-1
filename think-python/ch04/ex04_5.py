""" Think Python Chapter 4, Exercise 4.5 (p.38)
jvdoorne, @Syntra, 06/10/2022
"""
import turtle


def archimedean_spiral(t: turtle.Turtle):
    return None    # TODO


def logarithmic_spiral(t: turtle.Turtle):
    for i in range(1, 500):
        t.fd(2)
        t.rt(360 / i)


if __name__ == '__main__':
    turt_reynolds = turtle.Turtle()
    logarithmic_spiral(turt_reynolds)
    turt_reynolds.clear()
    # archimedean_spiral(turt_reynolds)
    turtle.mainloop()
