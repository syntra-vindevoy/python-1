a = int( input('a = ') )
b = int( input('b = ') )
c = int( input('c = ') )
n = int( input('n = ') )

def check_fermat(a, b, c, n):
    if n>2 and a**n + b**n == c**n:
        print("Gosh, Fermat got it wrong!")
    else:
        print("No, that won't work.")

check_fermat(a, b, c, n)