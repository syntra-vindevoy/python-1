"""
Exercise 1.2: Boek: Thinkpython2 p30

De Meyer Ronny
"""
print("1.")
minutes = 42
seconds = 42
print(f"Hoeveel seconden zijn er in totaal in {minutes} minuten en {seconds} seconden?")

total_seconds = (minutes * 60) + seconds
print(f"Totaal aantal seconden = {total_seconds}")

print("\n2.")
distance_km = 10
print(f"Hoeveel miles zijn er in {distance_km} km?")
distance_miles = distance_km / 1.61
print(f"Er zijn {round(distance_miles, 2)} miles in {distance_km} km")

print("\n3.")

def convert_km_to_mile(x):
    return x/1.61


def convert_minuten_and_seconds_to_seconds(minutes, seconds):
    return (minutes * 60) + seconds


def convert_seconds_to_minutes_and_seconds(total_seconds):
    minutes = total_seconds // 60
    seconds = total_seconds%60
    return minutes, seconds


distance_km = 10
minutes = 42
seconds = 42
total_seconds = convert_minuten_and_seconds_to_seconds(minutes, seconds)
print(f"total_seconds = {total_seconds}")
dintance_miles = convert_km_to_mile(distance_km)
print(f"dintance_miles = {dintance_miles}")
print(f"If you run a {distance_km} kilometer race in {minutes} minutes {seconds} seconds, what is your average pace (time per \
mile in minutes and seconds)? What is your average speed in miles per hour?")
average_pace_seconds = total_seconds / distance_miles
print(f"average_pace_seconds = {average_pace_seconds}")
average_pace = convert_seconds_to_minutes_and_seconds(average_pace_seconds)
print(f"average_pace ( time per mile ) = {average_pace[0]} minutes and {average_pace[1]} seconds")
average_speed = distance_miles / total_seconds * 3600
print(f"average speed is {average_speed} miles per hour")
