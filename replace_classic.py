import datetime

start = datetime.datetime.now()

for c in range(10000000):
    x = 10
    y = 12

    z = x
    x = y
    y = z

end = datetime.datetime.now()

print(x)
print(y)

print(end - start)
