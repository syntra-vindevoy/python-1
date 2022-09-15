#pagina 19 - oefening 3 van 2-2
#3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
#tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
#--> print(24720//3600) = 6 seconden

leave_house = (6*3600)+(52*60)
first_time = (8*60)+15
second_time = ((7*60)+12) * 3
thirth_time = (8*60)+15

time_home = leave_house + first_time + second_time + thirth_time
hour_home = time_home // 3600
minutes_home = (time_home % 3600) // 60
seconds_home = ((time_home % 3600) % 60)
print(hour_home)
print(minutes_home)
print(seconds_home)
print(time_home)