"""
5. van een woord of zin, zoek de kleinste en hoogste letter
verplicht loop
min/max verboden
"""
import string


# def pday(d):
#     if d < 10:
#         return f"0{d}"
#     else:
#         return str(d)
#
# ljust ( links alinieren)
# rjust ( rechts alinieren)


to_check = input('Geef een woord of zin in: ')

def klein_groot_ste_letter(string):
    # initializing a new string to apppend only alphabets
    to_test = ""
    # looping through the string to find out alphabets
    for char in string:
        # ord(chr) returns the ascii value
        # CHECKING FOR UPPER CASE
        if ord(char) >= 65 and ord(char) <= 90:
            to_test += char
        # checking for lower case
        elif ord(char) >= 97 and ord(char) <= 122:
            to_test += char
    print(f"Geldige letters in string = {to_test}")
    kleinste = to_test[0]
    for letter in to_test:
        if letter < kleinste:
            kleinste = letter
    print(f'Kleinste letter = {kleinste}')

    grootste = to_test[0]
    for letter in to_test:
        if letter > grootste:
            grootste = letter
    print(f'Grootste letter = {grootste}')

klein_groot_ste_letter(to_check)
