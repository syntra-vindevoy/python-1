def find_number(n):
    counter = 1
    lowest = 0
    highest = 1000000000
    guess = int((highest-lowest)/2)
    while lowest != highest:
        if guess < n:
            print(guess)
            lowest = int(guess)
            guess += int((highest-lowest)/2)
            counter += 1
        elif guess > n:
            print(guess)
            highest = int(guess)
            guess -= int((highest-lowest)/2)
            counter += 1
        else:
            print(f"The answer is {guess} and i found it in {counter} times")
            break
find_number(int(input("Enter a number between 0 and 10000: ")))
