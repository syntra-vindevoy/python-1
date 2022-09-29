def do_foortime(f):
    f()
    f()
    f()
    f()

def grid_h():
    print("+" + "-" * 4 + "+" + "-"*4 + "+")

def grid_v():
    print("|" + " " * 4 + "+" + " " *4 + "|")


grid_h()
do_foortime(grid_v)
grid_h()
do_foortime(grid_v)
grid_h()


























