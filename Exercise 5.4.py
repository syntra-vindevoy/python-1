def is_triangle(a,b,c):
    if a + b > c:
        print("no")
    if a + c > b:
        print("no")
    if b + c > a:
        print("no")

    else:
        print("Yes!")

def check_numbers():
    a = int(input("a?"))
    b = int(input("b?"))
    c = int(input("c?"))

check_numbers()