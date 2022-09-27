leavehousesec = 6*60*60+52*60
pacemilesec= 8*60+15
pace3milessec = 7*60+12
breakfast = leavehousesec+2*pacemilesec+3*pace3milessec

hours = int(breakfast)
minutes = (breakfast*60) % 60
seconds = (breakfast*3600) % 60

print("%1d:%02d.%02d" % (hours, minutes, seconds))
