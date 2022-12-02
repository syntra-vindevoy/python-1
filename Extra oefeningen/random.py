import random

a = random.randint(0, 20)

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