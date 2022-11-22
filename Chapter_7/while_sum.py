s = 0
n = -1

while n != 0:
    n = int(input("Geef een int van 1 tem 10, zn 0 om te eindigen"))
    s += n

print(f"\nDe som is: {s}")

## andere versie:
while True:  # -> je hoeft n niet meer vooraf te declareren
    n = int(input("Geef een int van 1 tem 10, zn 0 om te eindigen"))

    if n < 0 or n > 10:
        print("Verkeerde input")
        continue  # zo ga je terug naar je while

    if n == 0:
        break

    s += n

print(f"\nDe nieuwe som is: {s}")
