
"""
4. calculator
vraag bewerking
vraag waarde
voer bewerking uit
start waarde = 0
"""
startvalue = 0


def ask_operation():
    operation = -1
    while operation < 0 or operation > 6:
        try:
            operation = int(input("What operation would you like to do?\n1 = sum\n2 = subtract\n3 = multiply\n4 = devide\n5= stop\n: "))
        except:
            operation = int(input("What operation would you like to do?\n1 = sum\n2 = subtract\n3 = multiply\n4 = devide\n5= stop\n: "))
    return operation


def ask_number():
    number = 0
    try:
        number = float(input("Give the number: "))
    except:
        number = float(input("Give a valid number plz: "))
    return number


def calc(oper, x, y):
    if oper == 1:
        x += y
    elif oper == 2:
        x -= y
    elif oper == 3:
        x *= y
    elif oper == 4:
        x /= y
    elif oper == 5:
        x = x
    return x


result = ask_number()
oper = 1
while oper != 5:
    oper = ask_operation()
    if oper == 5:
        print(f'\neindresultaat = {result}')
        break
    numb = ask_number()
    result = calc(oper, result, numb)
    print(f'\ntussenresultaat = {result}')
