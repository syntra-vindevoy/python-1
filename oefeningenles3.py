import sys
def calculator(value1):
    print("select an operation to perform or type stop")
    print("+        -")
    print("*        /")
    operation = input()
    if operation == "+":
        answer = int(value1) + int(input("number 2: "))
        print(answer)
        calculator()
    elif operation == "-":
        answer = int(value1) - int(input("number 2: "))
        print(answer)
        calculator(int(input("mumber 1: ")))
    elif operation == "*":
        answer = int(value1) * int(input("number 2: "))
        print(answer)
        calculator(int(input("mumber 1: ")))
    elif operation == "/":
        answer = int(value1) / int(input("number 2: "))
        calculator(int(input("mumber 1: ")))
        print(answer)
        calculator()
    elif operation =="stop":
        sys.exit()
    else:
        print("invalid input")
calculator(int(input("mumber 1: ")))