import datetime

LOWER = 1
UPPER = 100000000


def search_recursive(number_to_guess: int, lower_boundary: int = LOWER, upper_boundary: int = UPPER, guesses: int = 0):
    # print(f"{number_to_guess} - {lower_boundary} - {upper_boundary} - {guesses}")

    middle = (lower_boundary + upper_boundary) // 2
    print(middle)
    guesses += 1

    if middle == number_to_guess:
        return middle, guesses

    if upper_boundary - lower_boundary == 1:
        return upper_boundary, guesses

    if middle > number_to_guess:
        return search_recursive(number_to_guess=number_to_guess, lower_boundary=lower_boundary, upper_boundary=middle,
                                guesses=guesses)
    else:
        return search_recursive(number_to_guess=number_to_guess, lower_boundary=middle, upper_boundary=upper_boundary,
                                guesses=guesses)


def search_while(number_to_guess: int, lower_boundary: int = LOWER, upper_boundary: int = UPPER, guesses: int = 0):
    # print(f"{number_to_guess} - {lower_boundary} - {upper_boundary} - {guesses}")

    while True:
        middle = (lower_boundary + upper_boundary) // 2
        guesses += 1

        if middle == number_to_guess:
            return middle, guesses

        if upper_boundary - lower_boundary == 1:
            return upper_boundary, guesses

        if middle > number_to_guess:
            upper_boundary = middle
        else:
            lower_boundary = middle


def main():
    method_to_use = search_recursive

    number, guesses = method_to_use(1)
    assert number == 1
    print(f"Found {number} in {guesses} guesses")

    return

    number, guesses = method_to_use(2)
    assert number == 2
    print(f"Found {number} in {guesses} guesses")

    number, guesses = method_to_use(9999)
    assert number == 9999
    print(f"Found {number} in {guesses} guesses")

    number, guesses = method_to_use(10000)
    assert number == 10000
    print(f"Found {number} in {guesses} guesses")

    max_number, max_guesses = method_to_use(LOWER)

    for n in range(LOWER, UPPER):
        # print(n)
        _, guesses = method_to_use(n + 1)

        if guesses > max_guesses:
            max_guesses = guesses
            max_number = n + 1

    print(f"It took {max_guesses} for number {max_number}")


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()

    print(end - start)
