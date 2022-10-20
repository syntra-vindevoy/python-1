import turtle

lengt = 500

def square (t, l):
    for _ in range (4):
        t.fd(lengt)
        t.lt(90)

if __name__=="__main__":

    bob = turtle.Turtle()
    square(bob,lengt)
    turtle.mainloop()





