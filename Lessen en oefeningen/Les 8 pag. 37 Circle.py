import turtle

bob = turtle.Turtle()
n = 360

for i in range(n):
    bob.fd(850 / n)
    bob.lt(450 / n)


print(bob)
turtle.mainloop()

