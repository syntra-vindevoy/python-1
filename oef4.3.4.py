# Write a function called circle that takes a turtle, t, and radius, r, as parameters and
#that draws an approximate circle by calling polygon with an appropriate length and
#number of sides. Test your function with a range of values of r.
#Hint: figure out the circumference of the circle and make sure that length * n =
#circumference.

import math
import turtle

hoeken = 360
radius = 10

lengt = (((radius**2)*math.pi) / hoeken)

print(lengt*hoeken)
print(radius*radius*math.pi)


def circle (t, l, n, r ):
    for _ in range (hoeken):
        t.fd(lengt)
        t.lt(360/hoeken)


if __name__=="__main__":

    bob = turtle.Turtle()
    circle (bob, lengt, hoeken, radius )
    turtle.mainloop()

