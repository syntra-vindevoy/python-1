import datetime
import time


def showtime():
    total_seconds = time.time
    print(total_seconds())
    print(type(total_seconds()))
    year = int(total_seconds()) / 60 / 60 /24 / 365
    print(int(year))
    print(type(year))
    print("year is " + str((1970+(int(year)))))

    #float_days = year - int(year)
    #print(float_days)

    days_after_epoch = int(total_seconds()) / 60 / 60 /24
    print("days after epos " + str(int((days_after_epoch))))

def showseconds():
    total_seconds = time.time
    print(total_seconds())
    seconds = int(total_seconds() % 60)
    print(seconds)


showtime()
showseconds()
