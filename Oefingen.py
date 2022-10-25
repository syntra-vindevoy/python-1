line = "- " * 4
space = "  " * 4

def draw_horizontal():
    to_print = ["+", line,"+", line,"+"]
    print(*to_print)
def draw_vertical():
    to_print = ["|",space,"|", space, "|"]
    print(*to_print)
def four_times(f):
    f()
    f()
    f()
    f()
def draw_grid():
    draw_horizontal()
    four_times(draw_vertical)
    draw_horizontal()
    four_times(draw_vertical)
    draw_horizontal()



print(draw_grid())




