s = 0
n = 1
while True:
    n = int (input(" geef een getal van 1 tot 10 en een 0 om te eindigen:"))

    if n < 0 or n > 10:
        print("verkeerde input")
        continue

    if n==0:
        break
    s += n
print(f"\nDe som is: {s}")

#if type (x) is not int