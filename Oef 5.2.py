import random



def check_fermat():
    a = random.randint(0,100)
    b = random.randint(0,100)
    c = random.randint(0,100)
    n = random.randint(2,100)
    if a ** n + b ** n == c ** n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("pass: " + "a = " + str(a) )




for _ in range(100):
    check_fermat()

print("Fermat was right")