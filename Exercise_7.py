

s = 0
n = -1
message = "Geef een getal van 1 tem 10, geef 0 om te eindigen: "
while True:
    n = input(message)
    try:
        n = int(n)
        message = "Geef een getal van 1 tem 10, geef 0 om te eindigen: "
    except:
        message = "Gij kieken! Ingave was GEEN GETAL!!! Geef een getal van 1 tem 10, geef 0 om te eindigen: "
        continue
    if n == 0:
        break
    if n > 10:
        message = "OMG! Ingave was te GROOT!!! Geef een getal van 1 tem 10, geef 0 om te eindigen: "
        continue
    if n < 0:
        message = "Amai zulle. Ingave was te KLEIN!!! Geef een getal van 1 tem 10, geef 0 om te eindigen: "
        continue
    s += n
print(f"Totaal van ingegeven getallen = {s}")


# dummyproof maken
# if type(x) is not int:
# break / continue = net zoals break maar start de while opnieuw
