import datetime

start = datetime.datetime.now()

for c in range(10000000):
    x = 10
    y = 12

    x = y - x
    y = y - x
    x = y + x

end = datetime.datetime.now()

print(x)
print(y)

print(end - start)
