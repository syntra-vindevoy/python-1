""" Think Python Chapter 7, Exercise 7.2 (p.69)
jvdoorne, @Syntra, 20/10/2022
"""


def eval_loop():
    e = ""    # Better way to do this?
    while True:
        to_evaluate = input("Enter string to evaluate: ")
        if "done" in to_evaluate.lower():
            return e
        e = eval(to_evaluate)
        print(e)


if __name__ == '__main__':
    eval_loop()
