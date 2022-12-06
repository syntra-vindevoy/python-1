from datetime import datetime


def isprime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


before = datetime.now()

som = 1

n = 3

while True:
    if isprime(n):
        som += 1
        if som == 10000:
            print(n)
            break
    n += 2

after = datetime.now()

print(after - before)