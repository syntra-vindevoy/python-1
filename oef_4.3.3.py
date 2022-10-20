import turtle

lengt = 50
hoeken = 5

def polygon (t, l, n ):
    for _ in range (n):
        t.fd(lengt)
        t.lt(360/n)

if __name__=="__main__":

    bob = turtle.Turtle()
    polygon (bob,lengt, hoeken)
    turtle.mainloop()