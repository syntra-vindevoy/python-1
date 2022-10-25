import time

time =  int(time.time())
day = time // (24 * 3600)
time %= (24 * 3600)
hour = time // 3600 + 2
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))