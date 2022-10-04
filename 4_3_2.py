import turtle


bob = turtle.Turtle()


n = 360

for _ in range(n):
    bob.fd(600 / n)
    bob.lt(360 / n)


turtle.mainloop()

#if __name__ == "__main__":

