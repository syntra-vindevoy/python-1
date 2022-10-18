import datetime

start = datetime.timedelta(hours=6, minutes=52)
slow = datetime.timedelta(minutes=8, seconds=15)
fast = datetime.timedelta(minutes=7, seconds=12)

#print(start + slow * 2 + fast * 3)


two_hours_later = datetime.timedelta(hours=2)
print(datetime.datetime.now() + two_hours_later)