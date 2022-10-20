"""
Exercise 1.1: Boek: Thinkpython2 p29

De Meyer Ronny
"""
print("1.")
print("Wat gebeurt er als een van de haakjes weggelaten wordt?")
print("We krijgen fout : SyntaxError: '(' was never closed")
print("of beide haakjes weglaten?")
print("We krijgen fout: SyntaxEror: Missing parenthesis in call to 'print'")
print("\n2.")
print("Wat gebeurt er als een van de quotes weg gelaten wordt?")
print("We krijgen fout: SyntaxError: unterminated string literal ( detected at line 10 )")
print("of beide quotes weglaten?")
print("We krijgen fout: NameError: name 'test' is not defined")
print("\n3.")
print("Wat gebeurt er als er een extra + teken voor een positief getal gezet wordt?")
resultaat = 2 ++ 2
print("2 ++ 2 = " + str(resultaat) + " : Resultaat wordt gewoon berekend")
print("\n4.")
print("Wat gebeurt er als er leading zeroes staan in pythoncode?")
variabele_1 = "09"
print(f"{variabele_1} geeft een fout: SyntaxError: leading zeros in decimal integer literals are nor permitted,...")
print("\n5.")
print("Wat gebeurt er als er geen operator tussen 2 getallen staat?")
print("We krijgen fout: SyntaxError: invalid syntax. Perhaps you forgot a comma?")
