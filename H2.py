minutes = 42
seconds = 42


# string ?
# not working code : assert type(minutes) is str, "moet string zijn"

# switch x and y with extra variable

x = 10
y = 12

xx = x
x = y
y = xx

print(x, y)

# other
x = 10
y = 12

y = y-x
x = x+y
y = x-y

print(x, y)

# other with tuple
x = 10
y = 12

x, y = y, x

print(x, y)

# other with XOR
# x = 6 = 110
# y = 2 = 010

# x = x ^ y
# y = x ^ y
# x = ...

# enkel voor freaks, niet kennen

print("exercise 2.2.1")
x = 5
volume = x * 4 / 3 * 3.1415 * x**2
print(volume)

print("exercise 2.2.2")
bookprice = 24.95
discount = 0.4
shippingcost_1 = 3
shippingcost_more = .75
copies = 60

total_prices = (copies * bookprice * (1-discount)) + (shippingcost_more * (copies -1) ) + shippingcost_1

print(total_prices)
print(round(total_prices,2))
print("price is " + str(round(total_prices,2)))


print("exercise 2.2.3")

easymileseconds = 2 * (8 * 60 + 15 )
hardmileseconds = 3* (3 * 7 + 12)
tijdstipgestart = 6 * 60 * 60 + 52 * 60


allseconds = easymileseconds + hardmileseconds + tijdstipgestart
print(allseconds)

end_hours = allseconds // 3600
end_minutes = (allseconds // 60)
end_seconds = allseconds - end_hours * 3600 - end_minutes * 60

print(end_hours)
print(end_minutes)
print(end_seconds)