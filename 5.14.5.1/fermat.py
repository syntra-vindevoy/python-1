import math

print("This program will test the fermat theorem. Please enter a, b, c and  n.")
a = int(input("enter a"'a = '))
b = int(input(enter'b = '))
c = int(input('c = '))
n = int(input('n = '))

def check_fermat(a,b,c,n):
    if n <= 2 or a == 0 or b == 0 or c == 0:
        print("No, that does not work, because n must be bigger then 2 and neither a nor b and c may be 0")
    elif a ** n + b ** n == c ** n:
         print("Holy smokes, Fermat was wrong!")
    else:
        print("Everythin allright for this set of a = %d, b = %d, c = %d and n = %d" % (a, b, c, n))
    return



print(check_fermat(a, b, c, n))
