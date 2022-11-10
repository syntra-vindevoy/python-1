# print(get_primes(1, 100))
primes = [x for x in range(2,100) if(all(x % j for j in range(2, x)))]

list = ""
for x in range(1, 100):
    if x in primes:
        temp = str(x) + " "
        list += temp
        print(list)
        list = ""
    else:
        temp = str(x) + " "
        list += temp
print(list)
