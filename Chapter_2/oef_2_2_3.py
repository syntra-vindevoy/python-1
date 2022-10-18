pace1 = 8*60 + 15 #seconds per mile
distance1 = 1
pace2 = 7*60 + 12
distance2 = 3
duration = 2*pace1*distance1 + pace2*distance2 #total duration of run in seconds
print(duration)
time = 6*3600 + 52*60
new_time = time + duration
print(new_time)
new_hour = new_time//3600
print(new_hour)
print(new_time%3600)
new_minutes = (new_time%3600)//60
print(new_minutes)
new_seconds = (new_time%3600)%60
print(new_seconds)
print(f"I get home at {new_hour}:{new_minutes}:{new_seconds}")

# TEST function newday
# 4 scenarios based on new_hours result
# new_hour <24 -> same day -> am of pm
# new_hour >24 -> .. day(s) later -> am of pm
#
def newday(x):
    if x < 24:
        if x < 12:
            print(f"I get home on the same day at {new_hour}:{new_minutes}:{new_seconds} am.")

        else: print(f"I get home on the same day at {new_hour%12}:{new_minutes}:{new_seconds} pm.")
    else:
        if x%24 < 12:
            print(f"I get home {x//24} day(s) later at {x%24}:{new_minutes}:{new_seconds} am.")
        else: print(f"I get home {x//24} day(s) later at {(x%24)%12}:{new_minutes}:{new_seconds} pm.")

newday(new_hour)











