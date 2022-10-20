seconds = 1
hours = seconds / (60*60)
seconds = seconds - hours*60*60
minutes = seconds / 60
seconds = seconds - minutes *60

time_left_house = 6 * hours + 52 * minutes

miles_run_easy_pace = 2 * (8 * minutes + 15 * seconds)

miles_run_fast_pace = 3 * (7 * minutes + 12 * seconds)


total_time_run = miles_run_easy_pace + miles_run_fast_pace + time_left_house
