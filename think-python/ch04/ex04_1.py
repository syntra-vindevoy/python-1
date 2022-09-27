""" Think Python Chapter 4, Exercise 4.1 (p.37)
jvdoorne, @Syntra, 27/09/2022
"""

if __name__ == '__main__':
    print("""Stack diagram:
    
    __main__:
        bob --> turtle.Turtle()

    circle:
        t --> bob
        r --> 100

    arc:
        t --> bob
        r --> 100
        a --> 360
    """)
