"""
2. Wat is het 10 000 st priemgetal
zo snel mogelijk berekenen
"""

import datetime as dt

all_primes = [2, 3]


def isprime(x):
    # if x is in our list of primes, then it's prime
    if x in all_primes:
        return True
    for p in all_primes:
        if x % p == 0:
            return False
    upper_limit = int(x**0.5+1)
    divisor = all_primes[len(all_primes)-1]+2
    while divisor < upper_limit:
        if isprime(divisor):
            all_primes.append(divisor)
        if x % divisor == 0:
            return False
        divisor = divisor + 2
    return True


val = int(input("How many primes to find? "))
my_primes = []
i = 2
start = dt.datetime.now()

while len(my_primes) < val:
    if isprime(i):
        my_primes.append(i)
    i += 1

end = dt.datetime.now()
print(my_primes[-1])
print(end - start)
