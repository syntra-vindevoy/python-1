import turtle
def square (t, l):
    for i in range(4):
        t.fd(l)
        t.lt(90)

if __name__ == "__main__":

    bob = turtle.Turtle()

    square(bob, 200)

    turte.mainloop()