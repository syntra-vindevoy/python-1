def is_triangle(a, b, c):
    if ( c >= a + b or a >= b + c or b >= a + c ):
        print("YES")
    else:
        print("NO")
def check_numbers():
    a = int(input("Side 1?"))
    b = int(input("Side 2?"))
    c = int(input("Side 3?"))
    return is_triangle(a, b, c)
check_numbers()

