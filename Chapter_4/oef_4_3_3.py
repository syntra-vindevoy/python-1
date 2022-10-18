import turtle

l = 200
corners = 5  # globale variabelen kan je hier definieren zodat je enkel hier moet aanpassen


# Do not touch the code below


def polygon(x, length, n):
    for _ in range(n):
        x.fd(length)
        x.lt(360 / n)


if __name__ == "__main__":
    t = turtle.Turtle()
    polygon(t, l, corners)

    turtle.mainloop()
