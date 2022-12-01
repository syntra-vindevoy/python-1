def find_number(n):
    counter = 1
    lowest = 0
    highest = 10000
    guess = int((highest-lowest)/2)
    while lowest != highest:
        if guess < n:
            lowest = int(guess)
            guess += int((highest-lowest)/2)
            counter += 1
        elif guess > n:
            highest = int(guess)
            guess -= int((highest-lowest)/2)
            counter += 1
        else:
            print(f"The answer is {guess} and i found it in {counter} times")
            break
find_number(int(input("Give a number between 0 and 10000: ")))
