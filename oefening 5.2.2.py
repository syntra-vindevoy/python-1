def fermat(a, b, c, n):
    if n > 2 and (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")

def numbers():
    a = int(input("Geef een cijfer a: "))
    b = int(input("Geef een cijfer b: "))
    c = int(input("Geef een cijfer c: "))
    n = int(input("Geef een cijfer n: "))
    return fermat(a, b, c, n)

numbers()