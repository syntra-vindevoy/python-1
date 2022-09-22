""" Think Python Chapter 2, Exercise 1.2 (p.10)
jvdoorne, @Syntra 22/09/2022
"""

# Answer 1: 2562 seconds.
race_duration = (42 * 60) + 42
print(f"Race duration: {race_duration} seconds")

# Answer 2: 6.21 miles.
miles_per_km = 1 / 1.61
race_kilometers = 10
race_miles = miles_per_km * race_kilometers
print(f"Race distance: {race_miles:.02f} miles")

# Answer 3: 6 minutes and 52 seconds
pace = (race_duration / race_kilometers) / miles_per_km
print(f"Average pace: {int(pace // 60):02d}:{int(pace % 60):02d}")
