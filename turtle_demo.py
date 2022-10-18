import turtle
bob = turtle.Turtle()

print(bob)

n = 360

for i in range(n):
    bob.fd(1200/n)
    bob.lt(360/n)


turtle.mainloop() #om kadertje open te houden


