def check_fermat():
    prompt_a = "Welk getal a? " #foutenafhandeling al aan userzijde indien mogelijk, zodat niet doorgaat naar server
    a = int(input(prompt_a))
    prompt_b = "Welk getal b? "
    b = int(input(prompt_b))
    prompt_c = "Welk getal c? "
    c = int(input(prompt_c))
    prompt_n = "Welk getal n? "
    n = int(input(prompt_n))
    formule = (a ** n + b ** n == c ** n)

    if n <= 2 or a == 0 or b == 0 or c == 0:
        print('No, that does not work, because n must be bigger then 2 and neither a nor b and c may be 0')
        return

    elif formule == True:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")


if __name__ == "__main__":
    check_fermat()
