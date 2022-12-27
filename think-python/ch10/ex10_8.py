""" Think Python Chapter 10, Exercise 10.8 (p.101)
jvdoorne, @Home, 27/12/2022
"""

from random import randint


def shared_birthdays(class_size=23) -> bool:
    birthdays = [randint(1, 366) for _ in range(class_size)]
    return len(birthdays) != len(set(birthdays))


def check_birthday_paradox(n_students: int, n_samples: int) -> float:
    # https://en.wikipedia.org/wiki/Birthday_problem
    shared = [shared_birthdays(n_students) for _ in range(n_samples)]
    return shared.count(True) / n_samples


if __name__ == '__main__':
    # Test
    assert check_birthday_paradox(23, 1000) > 0.49

    # Check class size 1-100
    for n in range(1, 101):
        chance = check_birthday_paradox(n, 100)
        print(f"n: {n} | chance: {chance*100:.0f}%")
