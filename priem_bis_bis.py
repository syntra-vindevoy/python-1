from datetime import datetime


def isprime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


before = datetime.now()

l=[2]
som =1
n =3

while len(l) <10000:
    for i in l:
        if n%i == 0:
            break


    else:
        l.append(n)


    n+=2


print(l[-1])








after = datetime.now()

print(after - before)