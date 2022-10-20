# 2. Add another parameter, named length, to square.
# Modify the body so length of the sides is length,
# and then modify the function call to provide a second argu‐ ment.
# Run the program again. Test your program with a range of values for length.
import turtle
bob = turtle.Turtle()
print(bob)


def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)


if __name__=="__name__":
    bob = turtle.Turtle()
    square(bob)
    turtle.mainloop()


print(bob)

