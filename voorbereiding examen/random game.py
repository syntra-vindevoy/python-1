from random import randint


def random_game():
    number = randint(1, 9)
    print(number)
    x = 11
    while x != number and x != 0:

        x = input("enter the number: ")
        if x == number or x == 0:
            print("you won")





random_game()
