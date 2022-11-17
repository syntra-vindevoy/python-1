def is_prime(n: int) -> bool:

    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


to_print = str()

for i in range(101):
    if is_prime(i):
        to_print += str(i) + "\n"
    else:
        to_print += str(i) + ", "

print(to_print)
