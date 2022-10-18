import turtle
bob = turtle.Turtle()
print(bob)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polygon(bob, 7, 70)

#loop om het venster open te houden
turtle.mainloop()