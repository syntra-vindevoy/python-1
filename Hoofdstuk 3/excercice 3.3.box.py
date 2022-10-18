def print_line(start_char, middle_char):
    print(start_char, middle_char * 4, end=" ")
    print(start_char, middle_char * 4, start_char)


def draw_grid():
    # print("+", "- " * 4, "+", "- " * 4, "+")
    print_line("+", "- ")
    # print("|", "  " * 4, "|", "  " * 4, "|")
    print_line("|", "  ")
    print_line("|", "  ")
    print_line("|", "  ")
    print_line("|", "  ")
    print_line("+", "- ")
    print_line("|", "  ")
    print_line("|", "  ")
    print_line("|", "  ")
    print_line("|", "  ")
    print_line("+", "- ")


if __name__ == "__main__":
    draw_grid()