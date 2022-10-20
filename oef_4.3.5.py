#. Make a more general version of circle called arc that takes an additional parameter
#angle, which determines what fraction of a circle to draw. angle is in units of degrees,
#so when angle=360, arc should draw a complete circle


import math
import turtle


angle = 180
radius = 12
hoeken = 360
lengt = (((radius**2)*math.pi) / hoeken)

print(lengt*hoeken)
print(radius*radius*math.pi)

def circle (t,l,n,r,a):
    for _ in range(angle):
        t.fd(lengt)
        t.lt(360/hoeken)

if __name__=="__main__":

    bob = turtle.Turtle()
    circle (bob, lengt, hoeken, radius, angle)
    turtle.mainloop()