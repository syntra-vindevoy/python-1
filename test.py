def istSchaltJahr (jahr):
    """Using the algorithm provided in the worksheet, this function determines whether any given year is a leap year or not"""
    if jahr%400==0:
        return True
    elif jahr%100==0:
        return False
    elif jahr%4==0:
        return True
    else:
        return False

def monatsLaenge(monat, jahr2):
    """This functions is for determining the length of any given month,
    the year is given as a parameter as well because in a leap year, February is a day longer
    What this function does, is checking in which one of the two lists
    (the first is for months that are 31 days long, the second is for months which are 30 days long)
    the month is in and returning 31 or 30, unless of course the given month is February in which case
    the function checkes whether the given year is a leap year or not and then returns 29 or 28 respectively.
    """
    liste1=[1,3,5,7,8,10,12]
    liste2=[4,6,9,11]
    if (monat!=2):
        for i in liste1:
            if monat == i:
                return 31
        for i in liste2:
            if monat == i:
                return 30
    elif istSchaltJahr (jahr2)==True:
        return 29
    else:
        return 28

def week_day (day, monat, jahr):
    """Using the formula provided in the worksheet,
    this function calculates the value 'd' for any given day of any month of any year and then returns the value."""
    if istSchaltJahr(jahr) == True:
        listek=[5, 1, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    else:
        listek=[6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    k=listek[monat-1]
    y=jahr%100
    c=jahr//100
    d=(day+k+y+y//4-2*(c%4))%7
    return d

def name_day(b):
    """This function just returns the name of the day of the week, which is the parameter b"""
    list=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return list[b-1]


def monat_name(m):
    """Similar to name_day, this function returns the name of the month which is the parameter m"""
    monate=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return monate [m-1]

def calendar (year):
    """Utilizing two for-loops, this function checks for every day of every month, whether or not it is the first day of the month,
    the last day of the week, the last day of the month, or the last day of the week and the first day of the month or
    the last day of the month and the last day of the week as wekk, to then place it appropriately in the printed line"""
    kalendarwoche=0
    for i in range (1,13):
        string = "        " + monat_name(i) + " " + str(year)
        wochennamen = "KW  " + "So  " + "Mo  " + "Di  " + "Mi  " + "Do  " + "Fr  " + "Sa  "
        print(string + "\n" + wochennamen)
        zaehler=0
        firstDay=week_day(1,i,year)
        n=0
        for j in range (1, monatsLaenge(i, year)+1):
            if zaehler==0:
                print('%02d' % (kalendarwoche), end=" ")
                if (j == 1):
                    while (n < firstDay):
                        n += 1
                        print("  ", end="  ")
                        zaehler+=1
                    if (firstDay==6):
                        print('%2d' % (j), end="  ")
                        print ("\n")
                    else:
                        print('%2d' % (j), end="  ")
                else:
                    print('%2d' % (j), end="  ")
                zaehler += 1
            elif zaehler!=6:
                print('%2d' % (j), end="  ")
                zaehler+=1
            if j==monatsLaenge(i, year) and week_day(j,i,year)!=6:
                print ("\n ")
            if week_day(j,i,year)==6:
                if j>1 and j!=monatsLaenge(i,year):
                    print('%2d' % (j), end="  " )
                    kalendarwoche+=1
                    zaehler=0
                    print("\n")
                elif j==monatsLaenge(i, year):
                    print('%2d' % (j), end="  ")
                    kalendarwoche+=1
                    print("\n")
                elif j==1:
                    kalendarwoche+=1
                    zaehler=0

calendar(2100)