from datetime import datetime


def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True


before = datetime.now()

som = 0

n = 1
while True:
    if isprime(n) == True:
        som += 1
        if som == 100000:
            print(n)
            break
        n += 1
    n+=1

after = datetime.now()

print(after - before)

