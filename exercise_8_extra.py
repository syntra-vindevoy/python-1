""""
print alle getallen van 1 tot 100, na elk priemgetal ga je naar een nieuwe lijn
1 2
3
4 5
6 7
8 9 10
"""


def get_primes(start, end):
    out = list()
    if start <= 1:
        start = 2
    sieve = [True] * (end + 1)
    for p in range(start, end + 1):
        if sieve[p]:
            out.append(p)
            for i in range(p, end + 1, p):
                sieve[i] = False
    return out


if __name__ == "__main__":
    primes = [x for x in range(2, 100) if(all(x % j for j in range(2, x)))]

    my_list = ""
    for x in range(1, 101):
        if x in primes:
            temp = str(x) + " "
            my_list += temp
            print(my_list)
            my_list = ""
        else:
            temp = str(x) + " "
            my_list += temp
    print(my_list)
