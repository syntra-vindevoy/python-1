import random
answer = random.randint(0, 10)
def gamblegame():
    guess = int(input("Give in a number between 0-10"))
    if guess == answer:
        print(f"Jackpot {answer} was the correct number")
    elif guess < answer:
        print("higher")
        gamblegame()
    else:
        print("lower")
        gamblegame()
gamblegame()