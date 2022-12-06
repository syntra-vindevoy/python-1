"""
3. random => neem int
maak een spelletje nummer raden
"""
import random

start = 1
stop = 10
number = 0
to_seek = random.randint(start, stop + 1)


while number != to_seek:
    number = int(input(f'Find the number from {start} to {stop} ( enter 0 to stop ): '))
    if number == 0:
        print("Better luck next time")
        break
    if number == to_seek:
        print(f"Gratz!!! The number was: {number}")
        break
    if number < to_seek:
        print("Need a higher number")
        continue
    else:
        print("Need a lower number")
        continue
