""" Think Python Chapter 3, Exercise 3.3 (p.27)
jvdoorne, @Home, 27/09/2022
Extra: added variable column/row dimensions.
"""


def grid_line(cols, width):
    """ Draws the horizontal line that borders a row. """
    return '+' + (' -' * width + ' +') * cols + '\n'


def grid_row(cols, width, height):
    """ Draws the lines that make up the 'body' of a row. """
    return ('|' + ('  ' * width + ' |') * cols + '\n') * height


def draw_grid(cols, rows, width=4, height=4):
    body = grid_row(cols, width, height) + grid_line(cols, width)
    print(grid_line(cols, width) + (body * rows))


if __name__ == '__main__':
    draw_grid(cols=2, rows=2)
    draw_grid(cols=4, rows=4)
