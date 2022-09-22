""" Think Python Chapter 2, Exercise 2.2 (p.19)
jvdoorne, @Syntra, 22/09/2022
"""

# from math import pi
pi = 3.1415

# 1.
r = 5.0
V = (4 / 3) * pi * (r ** 3)
print(f"1. The volume of a sphere with radius {r} is {V:.2f}")

# 2.
cover_price = 24.95
discount = 0.40
base_shipping = 3.00
plus_shipping = 0.75
copies = 60

# Cost books + cost shipping
cost = (copies * cover_price * (1 - discount)) + \
       (base_shipping + ((copies - 1) * plus_shipping))

print(f"2. Total cost for {copies} copies: {cost:.2f} USD")

# 3.
t0 = (6 * 3600) + (52 * 60)     # start
d1 = (8 * 60) + 15
d2 = ((7 * 60) + 12) * 3
t1 = t0 + d1 + d2 + d1          # stop

# Convert total seconds to hh:mm:ss
# Tried this first via repeated % and //, but this is way more elegant
# Divmod, Thanks Google!
mm, ss = divmod(t1, 60)
hh, mm = divmod(mm, 60)

print(f"3. Breakfast at {hh:02.0f}:{mm:02.0f}:{ss:02.0f}")
