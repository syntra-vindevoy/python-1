# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 21:04:00 2022

@author: SIDDMRO

Boek: Logica en computationeel denken
pagina 41 : oefeningen
"""

def p41_oef_1(A, B, C):
    D = A and B
    E = B or C
    return xor(D, E)


def p41_oef_2(A, B):
    D = xor(A, B)
    E = nand(A, D)
    F = not B
    return E or F


def p41_oef_3(A, B, C):
    D = xnor(A, B)
    E = not(D or B)
    return nand(E, C)


def p42_oef_4(A, B, C, D):
    E = A or B
    F = B and C
    G = xor(C, D)
    H = nand(E, F)
    J = not(F or G)
    return xnor(H, J)


def p42_oef_5(A, B, C, D):
    E = A or B
    F = A and E
    G = C and D
    H = G or D
    return xor(F, H)


def p43_oef_6(A, B, C, D):
    E = xor(A, B)
    F = nand(C, D)
    G = B or F
    H = E and G
    J = not(G or D)
    return xnor(H, J)


def p43_oef_7(A, B, C, D):
    E = A or B
    F = not(E or B)
    G = not C
    H = nand(C, D)
    J = nand(F, G)
    K = xnor(G, H)
    return xor(J, K)

# def p44_oef_8(A, B, C)
# gelijktaardig en dan alle moglijkheden aflopen en aanduiden welke juist zijn.

def xor(A, B):
    return A != B


def xnor(A, B):
    return not(xor(A, B))


def nand(A, B):
    return not(A and B)


# %% p41 oefening 1a
A = True
B = True
C = True
X = p41_oef_1(A, B, C)
print(f"p41 oefening 1a: X = {X}")

# p41 oefening 1b
A = True
B = True
C = False
X = p41_oef_1(A, B, C)
print(f"p41 oefening 1b: X = {X}")

# p41 oefening 1c
A = True
B = False
C = False
X = p41_oef_1(A, B, C)
print(f"p41 oefening 1c: X = {X}")

# %% p41 oefening 2a
A = True
B = True
X = p41_oef_2(A, B)
print(f"p41 oefening 2a: X = {X}")

# p41 oefening 2b
A = True
B = False
X = p41_oef_2(A, B)
print(f"p41 oefening 2b: X = {X}")

# p41 oefening 2c
A = False
B = False
X = p41_oef_2(A, B)
print(f"p41 oefening 2c: X = {X}")

# %% p41 oefening 3a
A = False
B = True
C = True
X = p41_oef_3(A, B, C)
print(f"p41 oefening 3a: X = {X}")

# p41 oefening 3b
A = True
B = False
C = True
X = p41_oef_3(A, B, C)
print(f"p41 oefening 3b: X = {X}")

# p41 oefening 3c
A = True
B = True
C = False
X = p41_oef_3(A, B, C)
print(f"p41 oefening 3c: X = {X}")

# %% p42 oefening 4a
A = True
B = False
C = True
D = True
X = p42_oef_4(A, B, C, D)
print(f"p42 oefening 4a: X = {X}")

# p42 oefening 4b
A = True
B = True
C = True
D = True
X = p42_oef_4(A, B, C, D)
print(f"p42 oefening 4b: X = {X}")

# p42 oefening 4c
A = False
B = False
C = False
D = False
X = p42_oef_4(A, B, C, D)
print(f"p42 oefening 4c: X = {X}")

# p42 oefening 4d
A = True
B = True
C = False
D = False
X = p42_oef_4(A, B, C, D)
print(f"p42 oefening 4d: X = {X}")

# p42 oefening 4e
A = False
B = True
C = False
D = True
X = p42_oef_4(A, B, C, D)
print(f"p42 oefening 4e: X = {X}")

# %% p42 oefening 5a
A = True
B = True
C = True
D = True
X = p42_oef_5(A, B, C, D)
print(f"p42 oefening 5a: X = {X}")

# p42 oefening 5b
A = True
B = True
C = False
D = True
X = p42_oef_5(A, B, C, D)
print(f"p42 oefening 5b: X = {X}")

# p42 oefening 5c
A = True
B = False
C = False
D = True
X = p42_oef_5(A, B, C, D)
print(f"p42 oefening 5c: X = {X}")

# p42 oefening 5d
A = False
B = False
C = False
D = True
X = p42_oef_5(A, B, C, D)
print(f"p42 oefening 5d: X = {X}")

# p42 oefening 5e
A = False
B = True
C = True
D = False
X = p42_oef_5(A, B, C, D)
print(f"p42 oefening 5e: X = {X}")

# %% p43 oefening 6a
A = False
B = True
C = True
D = True
X = p43_oef_6(A, B, C, D)
print(f"p43 oefening 6a: X = {X}")

# p43 oefening 6b
A = True
B = False
C = True
D = True
X = p43_oef_6(A, B, C, D)
print(f"p43 oefening 6b: X = {X}")

# p43 oefening 6c
A = True
B = True
C = False
D = True
X = p43_oef_6(A, B, C, D)
print(f"p43 oefening 6c: X = {X}")

# p43 oefening 6d
A = True
B = True
C = True
D = False
X = p43_oef_6(A, B, C, D)
print(f"p43 oefening 6d: X = {X}")

# p43 oefening 6e
A = False
B = False
C = False
D = True
X = p43_oef_6(A, B, C, D)
print(f"p43 oefening 6e: X = {X}")

# %% p43 oefening 7a
A = False
B = True
C = True
D = True
X = p43_oef_7(A, B, C, D)
print(f"p43 oefening 7a: X = {X}")

# p43 oefening 7b
A = True
B = False
C = True
D = True
X = p43_oef_7(A, B, C, D)
print(f"p43 oefening 7b: X = {X}")

# p43 oefening 7c
A = True
B = False
C = True
D = False
X = p43_oef_7(A, B, C, D)
print(f"p43 oefening 7c: X = {X}")

# p43 oefening 7d
A = False
B = True
C = False
D = True
X = p43_oef_7(A, B, C, D)
print(f"p43 oefening 7d: X = {X}")

# p43 oefening 7e
A = True
B = True
C = True
D = True
X = p43_oef_7(A, B, C, D)
print(f"p43 oefening 7e: X = {X}")

# %% p44 oefening 8
# oplossen via redenering geeft telkens maar 1 mogelijkheid
A = False
B = False
C = True
# is enige mogelijke oplossing

# %% oefening 9
A = False # is al zeker

