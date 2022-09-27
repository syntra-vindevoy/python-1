afstand = 10
time_min = 42
time_sec = 42
time_per_mile_sec = (((time_min * 60)+time_sec)/10)*1.61

time_per_mile_min = ((time_min + (time_sec/60))/10)*1.61

avg_speed_miles_per_hour = (60/(time_min + (time_sec / 60)))*(afstand/1.61)

print(time_per_mile_min)
print(time_per_mile_sec)
print(avg_speed_miles_per_hour)
