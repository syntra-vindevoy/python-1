""" Write a function that returns the n-th prime.
jvdoorne, @Syntra, 15/11/2022, @Home, 17/11/2022
    Assignment given 10/11/2022, but missed that class.
    Still, wanted to give this a try.
"""

import datetime    # To time my solution


def nth_prime_upper_bound(n) -> int:
    """ Calculates an upper bound for the nth prime, to be used as
    the max size of an Eratosthenes' sieve for finding that prime.
    Read: https://math.stackexchange.com/questions/1270814/bounds-for-n-th-prime

    Note:
        Wrote my solution, then realised I wasn't allowed to import math,
        so I found some implementations of ceil/log functions on StackOverflow
        Sorry, haha.
    """

    def ceil(x) -> int:
        """ Imitates the math.ceil function. """
        return int(-1 * x // 1 * -1)

    def log(x, n_terms=1000) -> float:
        """ Imitates the math.log function.
        (~Approximates using a Taylor/Maclaurin series of n terms.)
        """
        return n_terms * ((x ** (1 / n_terms)) - 1)

    return 100 if n < 6 else ceil(n * (log(n) + log(log(n))))


def sieve_of_eratosthenes(n) -> list:
    """ Implements a Sieve of Eratosthenes to generate n primes.
    Read: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    # Build list of prime candidates
    sieve = [True for _ in range(n)]
    sieve[0], sieve[1] = False, False
    # Multiples can't be primes, so mark them as False
    for i, prime in enumerate(sieve):
        if prime:
            for j in range(i ** 2, n, i):
                sieve[j] = False
    return sieve


def find_nth_prime(n) -> int:
    sieve_size = nth_prime_upper_bound(n)
    sieve = sieve_of_eratosthenes(sieve_size)
    primes = [i for i, x in enumerate(sieve) if x]
    return primes[n - 1]


if __name__ == '__main__':

    # 10.000th prime
    start = datetime.datetime.now()
    assert find_nth_prime(10000) == 104729
    print(datetime.datetime.now() - start)

    # 100.000th prime
    start = datetime.datetime.now()
    assert find_nth_prime(100000) == 1299709
    print(datetime.datetime.now() - start)
