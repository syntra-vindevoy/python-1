def fibo(n):
    if n < 2:
        return n

         return  fibo(n -1)+fibo(n-2)

if __name__ == "__main__":
    for i in range(20):

        print(fibo(i))




