# 0 1 2 3 4 5 6 7
# 0 1 1 2 3 5 8 13
def fibo(n):
        if n < 3:
            return 1
        return fibo(n-1) + fibo(n-2)
print (fibo(7))
