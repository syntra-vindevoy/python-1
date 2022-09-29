def do_fourtime(f):
    f()
    f()
    f()
    f()

def grid_h():
    print("+" + "-" * 4 + "+" + "-"*4 + "+")

def grid_v():
    print("|" + " " * 4 + "+" + " " *4 + "|")


grid_h()
if __name__ == "__main__":
    do_fourtime(grid_v)
grid_h()
if __name__ == "__main__":
    do_fourtime(grid_v)
grid_h()


































