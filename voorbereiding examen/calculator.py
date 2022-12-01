
def ask_operation():
    operation = 0
    number = 0
    total = 0
    while operation < 5:
        print(total)
        print("1.+ , 2.-, 3*, 4/, 5 to stop")
        operation = int(input("what will it be: "))
        number = int(input("number please"))


        if operation == 1:
            total = number + total

        if operation == 2:
            total = number - total

        if operation == 3:
            total = number * total

        if operation == 4:
            total = number / total

        if operation == 5:
            print ("stop")
    else:
        print("aborted")

ask_operation()