import turtle

bob = turtle.Turtle()

n = 360
for i in range(n):
    bob.fd(600 / n)  # lengte tekening
    bob.lt(360 / n)  # hoek waarin gedraaid wordt 1 = 1 graad

turtle.mainloop()
