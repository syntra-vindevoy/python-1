print("Wat wil je doen?")
print("1.+")
print("2.-")
print("3.*")
print("4./")
print("5.Stop")

while True:
    keuze = input("Kies 1 2 3 4 5: ")
    if keuze == "5":
        break

    if keuze in ("1", "2", "3", "4", "5"):
        num1 = float(input("Eerste nummer: "))
        num2 = float(input("Tweede nummer: "))

        if keuze == "1":
            print(num1 + num2)

        elif keuze == "2":
            print(num1 - num2)

        elif keuze == "3":
            print(num1 * num2)

        elif keuze == "4":
            print(num1 / num2)
