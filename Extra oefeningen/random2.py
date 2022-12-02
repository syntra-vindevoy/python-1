from random import randint

a = randint(0, 10001)

while True:
    guess = int(input("Enter number: "))
    if guess == a:
        print("You Win! ")
        break

    elif guess < a:
        print("Higher")

    else:
        print("Lower")
        continue