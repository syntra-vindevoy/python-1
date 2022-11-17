"""
Exercise 8.4. The following functions are all intended to check whether a string contains any
lowercase letters, but at least some of them are wrong. For each function, describe what the function
actually does (assuming that the parameter is a string).
"""
s = 'banana'

# def any_lowercase1(s):
#     for c in s:
#         if c.islower():
#             return True
#         else:
#             return False
#
# print(f"Heeft het woord' {s}' kleine letters? : {any_lowercase1(s)} ")
# """
# enkel de eerste letter wordt gecontroleerd, dan krijgen we al true of false en zijn we uit de for loop
# """
#

# def any_lowercase2(s):
#     for c in s:
#         if 'c'.islower():
#             return 'True'
#         else:
#             return 'False'
#
# print(f"Heeft het woord' {s}' kleine letters? : {any_lowercase2(s)} ")
# """
# enkel de letter c wordt gecontroleerd, niet het meegegeven woord dus geeft altijd een string True
# """


# def any_lowercase3(s):
#     for c in s:
#         flag = c.islower()
#     return flag
# print(f"Heeft het woord' {s}' kleine letters? : {any_lowercase3(s)} ")
# """
# enkel laatste letter wordt teruggemeld, de andere passeren te snel
# """


# def any_lowercase4(s):
#     flag = False
#     for c in s:
#         flag = flag or c.islower()
#     return flag
#
# print(f"Heeft het woord' {s}' kleine letters? : {any_lowercase4(s)} ")
# """
# werkt zoals het moet, als er 1 letter lower is wordt de True onthouden
# """
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

print(f"Heeft het woord' {s}' kleine letters? : {any_lowercase5(s)} ")
"""
vanaf er een letter niet lowercase is returnen we al False en gaan we uit de loop, enkel volledig lowercase woorden geven true
"""