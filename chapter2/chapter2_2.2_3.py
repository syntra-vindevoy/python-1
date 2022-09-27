from datetime import datetime, timedelta

start = datetime.strptime("6:52 AM", "%I:%M %p")

easy_pace = 8*60 + 15
tempo = 7*60 + 12

print(start + timedelta(seconds=easy_pace * 2 + tempo * 3))


