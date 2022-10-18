import turtle

bob = turtle.Turtle()

n = 1440

for i in range(n):
    bob.fd(800 / n)
    bob.lt(360 / n)

turtle.mainloop()
