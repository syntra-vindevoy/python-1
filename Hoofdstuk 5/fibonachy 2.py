# 0 1 2 3 4 5 6 7
# 0 1 1 2 3 5 8 13
def fibo (n):
        if n < 2:
            return n

        return fibo(n-1) + fibo(n-2)
if __name__ == "__main__":
    for i in range(11):
        print(fibo(i))