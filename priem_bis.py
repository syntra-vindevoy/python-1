from datetime import datetime


def isprime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
before = datetime.now()

som = 0
m = 0
pr = []
a = [m * 10 + 2 + s for s in range(0, 10)]
# print(a)

while True:
    b = [m * 100 + 2 + s for s in range(0, 100)]
    # print(b)
    for z in pr:
        # print(z)
        for y in b:
            # print(z)
            # print(y % z)
            if y % z == 0:
                b.remove(y)
                # print(b)
    while len(b) != 0:
        c = b[0]
        pr.append(c)
        som += 1
        if som == 10000:
            print(c)
            break
        # print(som)
        #print(pr)
        b = [x for x in b if x % c != 0]
        # print(b)
    if som == 10000:
        break
    m += 1

    # print(b)
    # while len(b)!= 0:
    # pr = pr.append

    # while len(a) != 0:
    # h



after = datetime.now()

print(after - before)

print(isprime(1))
