def is_triangle():
    prompt_a = "Welk getal a? "
    a = int(input(prompt_a))
    prompt_b = "Welk getal b? "
    b = int(input(prompt_b))
    prompt_c = "Welk getal c? "
    c = int(input(prompt_c))

    # if (a > b + c or b > a + c or c > a + b):
    #    return False
    # return true

    if a > b + c:
        print("No")
    elif b > a + c:
        print("No")
    elif c > a + b:
        print("No")
    else:
        print("yes")


if __name__ == "__main__":
    is_triangle()
