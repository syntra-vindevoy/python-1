
def print_grid(area, unit):
    for _ in range(area):
        print(("+" + "- " * unit) * area + "+")
        for _ in range(unit):
            print(("|" + "  " * unit) * area + "|")
    print(("+" + "- " * unit) * area + "+")


if __name__ == "__main__":

    print_grid(5,3)