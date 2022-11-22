import  math
def eval_loop():
    while True:
        a=input('Enter the expression to evaluate (or enter "done" to stop): ')
        if a=='done':
            break
        else:
            y=eval(a)
            print(y)
    print(y)
eval_loop()