s = 0

while True:
    n = int(input("Geef een int van 1 t/m 10, 0 om te eindigen: "))

    if n < 0 or n > 10:
        print("Verkeerde input")
        continue

    if n == 0:
        break

    s += n

print(f"\nDe som is: {s}")
