# algemene oefening op bord
# x = 10  , y = 12 print waarden X en Y die verwisseld zijn van plaats

x = 10
y = 12
# old_x = x
# x = y
# y = old_x
# print(f"x = {x}")
# print(f"y = {y}")

# wisselen met definitie
def wissel_x_y(x, y):
    return y, x

temp = wissel_x_y(x, y)
x = temp[0]
y = temp[1]
print(f"x = {x}")
print(f"y = {y}")

# 1 lijn:
x, y = y, x


# met XOR ook mogelijk

x = x ^ y
y = x ^ y
x = x ^ y
