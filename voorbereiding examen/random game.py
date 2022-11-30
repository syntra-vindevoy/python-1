from random import randint


def random_game():
    number = randint(1, 9)
    x = 11
    while number != x :
        print(x)
        print(number)
        x = int(input("enter the number: "))
        if  x == 0:
            print("you quit")
            break

    print("you won")


random_game()
