import turtle


length = 100
corner = 9



def polygon(t, l, n):
    for _ in range(n):
        t.fd(l)
        t.lt(360 / n)



if __name__ == "__main__":
    bob = turtle.Turtle()
    polygon(bob, length, corner)

    turtle.mainloop()