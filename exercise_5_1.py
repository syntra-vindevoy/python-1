"""Exercise 5.1. The time module provides a function, also named time, that returns the current
Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. On
UNIX systems, the epoch is 1 January 1970.
import time
time.time()
1437746094.5735958
Write a script that reads the current time and converts it to a time of day in hours, minutes, and
seconds, plus the number of days since the epoch.
voor de komma = dag, na de komma = uur, minuten en seconden
"""
import datetime
import pytz as pytz
import time

epoch_time = 1437746094.5735958

# using datetime.fromtimestamp() function to convert epoch time into datetime object
mytimestamp = datetime.datetime.fromtimestamp(epoch_time)

# using strftime() function to convert
datetime_str = mytimestamp.strftime("%Y - %m - %d  %H : %M : %S")

# printing the values
print("Given epoch time:", epoch_time)
print("Converted datetime string:", datetime_str)


def epoch():
    tz = pytz.timezone("UTC")
    print(f"now: {datetime.datetime.now().astimezone(tz=tz)}")


print("2e poging")

time_now = time.time()
print(f"time now is: {time_now}")
epoch_time = time_now

days = epoch_time // (60 * 60 * 24)
remaining_epoch = epoch_time - (days * 60 * 60 * 24)
hours = remaining_epoch // (60 * 60)
remaining_epoch = remaining_epoch - (hours * 60 * 60)
minutes = remaining_epoch // 60
seconds = int(remaining_epoch - (minutes * 60))

print(f"epoch time = {epoch_time} , this is {days} days, {hours} hours, {minutes} minutes and {seconds} seconds ago")
