def fibo(n):
    if n < 2:
            return n
    n_min_2 = 0
    n_min_1 = 1

    for i in range(n - 1):
        n_min_1, n_min_2 = n_min_1 + n_min_2 , n_min_1

    return n_min_1

r= fibo(500)

print(r)