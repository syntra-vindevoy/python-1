import math
import turtle
length = 100
corners = 5
def square(t,l):
    for i in range(4):
        t.fd(l)
        t.lt(90)
def polygon(t,l,n
    for i in range(n):
        t.fd(l)
        t.lt(360/n)
def circle(t, r):
    m = r * 2 * math.pi
    for i in range(360):
        t.fd(n/360)


if __name__ == '__main__':
    bob = turtle.Turtle()
    polygon(bob, length, corners)

    turtle.mainloop()