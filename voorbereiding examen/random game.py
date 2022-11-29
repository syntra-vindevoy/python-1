from random import randrange

def random_game():
    number = randrange.randint(1, 9)

    while input() != number and input():
        continue
