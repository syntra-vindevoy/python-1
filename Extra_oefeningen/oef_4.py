# calculator

print("Welcome to the CALCULATOR.. Starting value = 0")
a = 0
while True:
    print("Please enter desired operation:")
    operation = input("1 for adding, 2 for substracting, 3 for multiplying, 4 for dividing, or Enter 0 to exit..\n")
    if operation == "0":
        break
    else:
        value = int(input("Enter value: "))

        if operation == "1":
            a += value
        if operation == "2":
            a -= value
        if operation == "3":
            a *= value
        if operation == "4":
            a /= value
        print(f"New value is: {a}")

print(f"final value is {a}")



