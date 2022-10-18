import turtle
oef nog te maken
#def circle(t, r, ):



def polygon(t, len, n):  # hier wordt bob parameter t
    for _ in range(n):
        t.fd(len)
        t.lt(360/n)


def square(t, len):  # hier wordt bob parameter t
    for _ in range(4):
        t.fd(len)
        t.lt(90)


if __name__ == "__main__":
    length = 200
    n = 360
    corners = 5
    bob = turtle.Turtle()
    #circle(bob)
    polygon(bob, length, corners)  # bob wordt parametere voor t
    square(bob, length)  # bob wordt parametere voor t
    turtle.mainloop()

