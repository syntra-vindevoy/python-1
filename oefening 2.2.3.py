#3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
#tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

leave_house = (6*3600)+(52*60)  #reken in seconden, 1uur heeft 3600 seconden en 1 minuut heeft 60 seconden
first_time = (8*60)+15
second_time = ((7*60)+12) * 3    # de *3 is omdat hij 3 mijl heeft gelopen aan dit tempo
thirth_time = (8*60)+15

time_home = leave_house + first_time + second_time + thirth_time # hoeveel seconden is de dag al bezig sinds middernacht
hour_home = time_home // 3600    # // is een deling maar de restwaarde word overboord gegooid
minutes_home = (time_home % 3600) // 60 # % is een deling maar enkel de rest waarde is de uitkomst
seconds_home = ((time_home % 3600) % 60)
print(f"{hour_home} uur")
print(f"{minutes_home} minuten")
print(f"{seconds_home} seconden")
print(time_home)


