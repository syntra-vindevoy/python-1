
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Wat wil je doen?")
print("1.+")
print("2.-")
print("3.*")
print("4./")
print("5.Stop")

while True:
    # take input from the user
    keuze = input("Kies 1 2 3 4 5: ")
    if keuze == "5":
        break

    if keuze in ("1", "2", "3", "4", "5"):
        num1 = int(input("Eerste cijfer: "))
        num2 = int(input("Tweede cijfer: "))

        if keuze == "1":
            print(add(num1, num2))

        elif keuze == "2":
            print(subtract(num1, num2))

        elif keuze == "3":
            print(multiply(num1, num2))

        elif keuze == "4":
            print(divide(num1, num2))
