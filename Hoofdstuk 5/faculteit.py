from datetime import datetime

def fac (n: int ) -> int:
    for i in range(2, n):
        #nvermenigvuldigd met i en zet waarde in n
        n *= i

    return n

if __name__ == "__main__":

    start = datetime.now()

    for _ in range(5000000):
        fac(10)

    end = datetime.now()

    print (end - start)