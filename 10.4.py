t = [1,2,3,4,5,6]
def chop(t):
    del t[0]
    del t[-1]
    print(t)

chop(t)
