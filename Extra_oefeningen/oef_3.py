# random spelletje

import random

# random.randint() method is used to generate random integers between the given range.
a = random.randint(0, 10)
while True:
    print(a)
    prompt = int(input("Please guess a number between 0 and 10, enter -1 to exit: "))
    if prompt == a:
        print("Correct")
        break
    if prompt == -1:  #
        print("exit")
        break
    else:
        print("Guess higher"*(prompt < a) + "Guess lower"*(prompt > a))




