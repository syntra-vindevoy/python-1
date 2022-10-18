#If I leave my house at 6:52 am and run 1 mile at an easy pace
# (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile
# at easy pace again, what time do I get home for breakfast?

SECONDS = 1
MINUTES = 60 * SECONDS
HOURS = 60 * MINUTES

time_left_house = 6 * HOURS + 52 * MINUTES

miles_run_easy_pace = 2 * (8 * MINUTES + 15 * SECONDS)

miles_run_fast_pace = 3 * (7 * MINUTES + 12 * SECONDS)

time_returned_home = miles_run_easy_pace + miles_run_fast_pace + time_left_house

hours = time_returned_home // HOURS
part_hour = time_returned_home % HOURS
minutes = part_hour // MINUTES
seconds = part_hour % MINUTES

print("Time returned home:", hours,":", minutes,":", seconds,"am")