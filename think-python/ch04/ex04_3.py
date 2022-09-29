""" Think Python Chapter 4, Exercise 4.3 (p.37)
jvdoorne, @Syntra, 29/09/2022
"""

import math
import turtle


def pie(t: turtle.Turtle, l, n):
    """
    Uses a Turtle to draw a polygon with n segments and spoke length l.
    """
    # Each segment is an isosceles triangle (NL: gelijkbenige driehoek)
    top_angle = 360 / n
    base_angle = (180 - top_angle) / 2
    # Each segment can be split again into 2 right-angled triangles,
    # so we can use sin(1/2 top angle, IN RAD) == 1/2 base length / l
    # to calculate the full base length.
    top_rad = top_angle / 2 * (math.pi / 180)    # Convert to radians
    base_length = l * math.sin(top_rad) * 2
    # Go Turtle, go!
    for _ in range(n):
        t.fd(l)
        t.lt(180 - base_angle)
        t.fd(base_length)
        t.lt(180 - base_angle)
        t.fd(l)
        t.lt(180)


if __name__ == '__main__':
    turt_reynolds = turtle.Turtle()    # Hehe
    # Figure 4.2, pie 1
    pie(turt_reynolds, 100, 5)
    turt_reynolds.clear()
    # Figure 4.2, pie 2
    pie(turt_reynolds, 100, 6)
    turt_reynolds.clear()
    # Figure 4.2, pie 3
    pie(turt_reynolds, 100, 7)
    turt_reynolds.clear()
    turtle.mainloop()
