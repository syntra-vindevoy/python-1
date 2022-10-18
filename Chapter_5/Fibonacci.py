from datetime import datetime


def fibo_recur(n):
    if n < 2:
        return n
    return fibo_recur(n - 1) + fibo_recur(n - 2)


def fibo_range(n):
    if n < 2:
        return n
    else:
        a = 1
        b = 1
        for i in range(n - 2):
            # b, a = b+a, b  -> dit is via tuple
            c = a + b
            a = b
            b = c
        return b


if __name__ == "__main__":

    prompt = "Welk getal van Fibonacci (recursief) printen? "
    nummer = int(input(prompt))
    start_1 = datetime.now()
    print(fibo_recur(nummer))
    end_1 = datetime.now()
    print(end_1 - start_1)

    prompt_2 = "Welk getal van Fibonacci (loop) printen? "
    nummer_2 = int(input(prompt_2))
    start_2 = datetime.now()
    print(fibo_range(nummer_2))
    end_2 = datetime.now()
    print(end_2 - start_2)

    import math
    print(int(math.log10(fibo_range(nummer_2)))+1) # dit berekent het aantal cijfers in een getal


