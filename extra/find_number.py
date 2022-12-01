""" Write a function that searches a number in a range between two
constants (MIN and MAX), and also reports the number of guesses it
took to find that number.

jvdoorne, @Syntra, 01/12/2022, extra exercise to prepare for exam.
"""

import datetime as dt   # To time solution
from random import randint

MIN, MAX = 1, 10000


def find_number(n: int, low: int = MIN, high: int = MAX) -> tuple:
    """ Checks if a number is present in a range between two given
    integers. Also returns the number of attempts it took to find
    that number. (basically implements an iterative binary search)
    """
    attempts = 0
    while low <= high:
        attempts += 1
        guess = low + (high - low) // 2
        if guess == n:
            return True, attempts
        elif guess < n:
            low = guess + 1
        else:
            high = guess - 1
    return False, attempts


""" Some tests. """


def test_all_numbers() -> None:
    print(f"\n[TEST] - Find ALL numbers between {MIN} and {MAX}:")

    t0 = dt.datetime.now()

    max_guesses = 0
    for i in range(MIN, MAX + 1):
        found, a = find_number(i)
        max_guesses = a if a > max_guesses else max_guesses
        assert found, f"Number {i} not found!"

    t1 = dt.datetime.now()

    print(f"All numbers between {MIN} and {MAX} were found. in {t1-t0}")
    print(f"This took a maximum of {max_guesses} attempts per number.")


def test_random_numbers(n=10) -> None:
    print(f"\n[TEST] - Find {n} random numbers between {MIN} and {MAX}:")

    for _ in range(n):
        to_find = randint(MIN, MAX+1)
        found, a = find_number(to_find)
        assert found, f"Random number {to_find} not found."
        print(f"Random number {to_find} found in {a} attempts.")


def test_some_numbers(t: tuple) -> None:
    print(f"\n[TEST] - Find some à la carte numbers: {t}")

    for n in t:
        found, a = find_number(n)
        print(f"Number: {n}, Found: {found}, Attempts: {a}")


if __name__ == '__main__':
    test_all_numbers()
    test_random_numbers(10)
    test_some_numbers((1, 2, 5000, 9999, 10000, 10001))    # Expect False for 10001 if MAX <= 10000
