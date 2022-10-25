import math


def eval_loop():
    while True:
        calc = input("Geef een bewerking in: ")

        if calc == "done":
            break

        print(eval(calc))


if __name__ == "__main__":
    eval_loop()