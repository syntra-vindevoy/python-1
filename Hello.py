start = (6*60+52)*60
ez_pace = (8*60+15)*2
fast_pace =(7*60+12)*3
total_seconds = start + ez_pace + fast_pace
end_hour =int(total_seconds/60/60)
end_minute = int((total_seconds/60) - end_hour*60)
end_second = int(total_seconds) - end_hour*60*60 - end_minute*60
print(end_hour,'hours',end_minute,'minutes',end_second,'seconds')