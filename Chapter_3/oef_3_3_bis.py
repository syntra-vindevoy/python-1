
def print_hor(h,v,s):
    print(("+"+s*"-")*h + "+")

print_hor(4,4,4)

def print_ver(h,v,s):
   print(("|"+s*" ")*h + "|")
print_ver(4,4,4)

def print_ver_four():
    print_ver(2,2,4)
    print_ver(2, 2, 4)
    print_ver(2, 2, 4)
    print_ver(2, 2, 4)

#print_ver_four()

def print_upper():
    print_hor(2,2,4)
    print_ver_four()

def print_grid():
    print_upper()
    print_upper()
    print_hor(2,2,4)

print_grid()



