""" calculate the average speed."""
sec_to_hr = 1/3600 # 3600 seconds in 1 hour
min_to_hr = 1/60 # 60 minutes in 1 hour
km_to_miles = 0.62 # 0.62 miles in 1 kilometer

time_hrs = 0+ (42*min_to_hr)+ (42*sec_to_hr) # Total time in hours
dist_miles = 10 * km_to_miles # Total time in miles

av_speed = dist_miles/time_hrs # Average Speed in miles/hour

answer1 = "Average speed = {} miles per hour".format(round(av_speed,2))

print(answer1)

"""
"Pace" is how much time in 1 mile. Time = Distance / Speed 
Also, Do you know what the function "round()" is doing?
"""
pace_dist = 10 # In 1 mile

pace_time_hr = round(pace_dist/av_speed, 2)
pace_time_min = round(pace_time_hr * 60, 2)
pace_time_sec = round(pace_time_min % 1,2) * 60

answer2 = "Average pace per mile = {} minutes and {} seconds".format(int(pace_time_min), int(pace_time_sec))
print(answer2)