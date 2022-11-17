def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))


def fibO_not_recursive(n):

    list_fibo = [0, 1]
    x = 0
    while (len(list_fibo)) < n:
        list_fibo.append(list_fibo[x] + list_fibo[x+1])
        x += 1

    return list_fibo


print(fibO_not_recursive(5))







