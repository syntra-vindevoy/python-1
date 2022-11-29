from random import randint

def random_game():
    number = randint(1, 9)

    while input() != number and input() != 0:
        continue
    print("fuck you won")

random_game()