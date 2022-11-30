from random import randint


def random_game():
    number = randint(1, 9)
    x = 11
    while number != x and x != 0:
        print(x)
        print(number)
        x = input("enter the number: ")
    print("you won")


random_game()
