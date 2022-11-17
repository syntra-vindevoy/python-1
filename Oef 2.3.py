
print("exercise 2.2.3")

easy_mile_seconds = 2 * (8 * 60 + 15)
hard_mile_seconds = 3 * (3 * 7 + 12)
start_time = 6 * 60 * 60 + 52 * 60
#all_seconds = 0
#end_seconds = 0

all_seconds = easy_mile_seconds + hard_mile_seconds + start_time
print(all_seconds)

end_hours = all_seconds // 3600
end_minutes = (all_seconds - ( end_hours * 3600 )) // 60
end_seconds = all_seconds - end_hours * 3600 - end_minutes * 60

print(end_hours)
print(end_minutes)
print(end_seconds)
