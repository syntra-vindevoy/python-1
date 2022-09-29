from datetime import datetime, timedelta

start = datetime.strptime("6:52 AM", "%I:%M %p")

easy_pace = 8*60 + 15
tempo = 7*60 + 12

print(start + timedelta(seconds=easy_pace * 2 + tempo * 3))

# without datetime

start = (6 * 60 + 52) * 60

end = start + 2 * easy_pace + 3 * tempo

time_h = end // 3600

time_min = (end % 3600) // 60

time_sec = (end % 3600) % 60

print(f"{time_h}:{time_min}:{time_sec} AM")

