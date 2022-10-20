import turtle
import math
bob = turtle.Turtle()

def square(t, lenght, n):
    angle = 360 / n
    for i in range(n):
         bob.fd(lenght)
         bob.lt(angle)

def circle(t, r):
    circumference = 2 * math.pi*r
    n = 50
    lenght = circumference / n

    square(t, lenght, n)


print(circle(turtle,35))
turtle.mainloop()




