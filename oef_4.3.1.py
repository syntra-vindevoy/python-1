import turtle


def square (t):
    for __ in range (4):
        t.fd(100)
        t.lt(90)

if __name__=="__main__":


    square(turtle.Turtle())
    turtle.mainloop()


