start_time_hours = 6
start_time_minutes = 52

easy_pace_minutes = 8
easy_pace_seconds = 15

fast_pace_minutes = 7
fast_pace_seconds = 12

start_time = start_time_minutes * 60 + start_time_hours * 3600
duration = (easy_pace_seconds * 2 + fast_pace_seconds * 3) + (easy_pace_minutes * 60 * 2 + fast_pace_minutes * 60 * 3)

end_time_seconds = start_time + duration
end_time_hours = end_time_seconds // 3600
end_time_seconds = end_time_seconds - end_time_hours * 3600
end_time_minutes = end_time_seconds // 60
end_time_seconds = end_time_seconds - end_time_minutes * 60

print(f'arrival at {end_time_hours}h {end_time_minutes}m {end_time_seconds}s')
