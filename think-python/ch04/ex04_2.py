""" Think Python Chapter 4, Exercise 4.2 (p.37)
jvdoorne, @Syntra, 27/09/2022
"""

from polygon import arc, turtle


def petal(t: turtle.Turtle, angle, radius):
    for _ in range(2):
        arc(t, radius, angle)
        t.lt(180 - angle)    # Turn for next petal-half


def flower(t: turtle.Turtle, n_petals, petal_angle, petal_radius):
    for _ in range(n_petals):
        petal(t, petal_angle, petal_radius)
        t.lt(360 / n_petals)    # Turn for next petal


if __name__ == '__main__':
    turt_reynolds = turtle.Turtle()    # Hehe
    # Figure 4.1, flower 1
    flower(turt_reynolds, 7, 60, 100)
    turt_reynolds.clear()
    # Figure 4.1, flower 2
    flower(turt_reynolds, 10, 60, 100)
    turt_reynolds.clear()
    # Figure 4.1, flower 3
    flower(turt_reynolds, 10, 60, 100)
    turtle.mainloop()
