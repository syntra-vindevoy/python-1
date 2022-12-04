from datetime import datetime


def is_prime(number: int, primes: list[int]):
    for prime in primes:
        if prime * prime > number:
            return True

        if number % prime == 0:
            return False

    return True


def main():
    find = 10000000

    find -= 1  # 2 we don't care for searching, it's the only even number to take into account
    primes = []
    number = 3
    counter = 0

    while counter < find:
        if is_prime(number=number, primes=primes):
            primes.append(number)
            counter += 1

        number += 2

    print(number - 2)


if __name__ == "__main__":
    start = datetime.now()
    main()
    end = datetime.now()

    print(end - start)