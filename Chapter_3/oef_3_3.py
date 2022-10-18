def hor_upper(v, s):
    return (("+"+s*"-")*v + "+\n")


def ver_upper(v, s):
    return ((("|"+s*" ")*v) + "|\n")*s


def draw_grid(h, v, s):
    grid = (hor_upper(v, s)+ver_upper(v, s))*h+(("+"+s*"-")*v + "+")
    print(grid)


if __name__ == "__main__":
    draw_grid(2, 4, 3)
