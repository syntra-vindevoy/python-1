"""
2. Wat is het 10 000 st priemgetal
zo snel mogelijk berekenen
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""
import datetime as dt


def primes(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n % 6 + 6, 2-(n % 6 > 1)
    sieve = [True] * (n // 3)
    for i in range(1, int(n ** 0.5) // 3+1):
      if sieve[i]:
        k = 3 * i + 1 | 1
        sieve[k * k // 3::2 * k] = [False] * ((n // 6 - k * k // 6 - 1) // k + 1)
        sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = [False] * ((n // 6 - k * (k - 2 * (i & 1) + 4) // 6 - 1) // k + 1)
    return [1, 2, 3] + [3 * i + 1 | 1 for i in range(1, n // 3 - correction) if sieve[i]]


start = dt.datetime.now()
test = primes(104724)
end = dt.datetime.now()
print(test[9999])
print(end - start)

# 10000 = 104723
# 100000 = 1299709
