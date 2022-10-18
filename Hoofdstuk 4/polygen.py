import turtle

lengt = 200
corners = 4

def polygon(t,l,n):
    for i in range(n):
        t.fd (l)
        t.lt (360/n)

if __name__ =="__main__":

    bob = turtle.Turtle()

    polygon(bob, lengt, corners)

    turtle.mainloop()
