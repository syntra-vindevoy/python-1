import random
def find_number(n):
    outcome = n
    count = 0
    lower = 1
    upper = 10001
    while True:
        guess = (lower + upper) // 2
        count += 1
        if guess == outcome:
            print(f" Value is: {guess}, was found in {count} times")
            return guess
        elif guess < outcome:
            lower = guess
        elif guess > outcome:
            upper = guess

if __name__ == "__main__":
    random.seed(0)
    a = random.randint(1, 10000)
    print(a)
    find_number(899)
    assert find_number(1) == 1
    assert find_number(2) == 2
    assert find_number(5000) == 5000
    assert find_number(9999) == 9999
    assert find_number(10000) == 10000
