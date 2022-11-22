def draw_grid(h, v, s):
    pass


def print_upper(v, s):
    for i in range(v):
        print("+" + s * "-", end="")
    print("+\n", end="")

print_upper(5,6)

def print_vert(v,s):
    for i in range(s):
        for j in range(v):
            print("|"+s*" ", end="")

        print("|\n", end="")

print_vert(5,6)