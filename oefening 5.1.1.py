import time

last_epoch = time.time()


def current_time(since_epoch):
    hours_since = since_epoch // 60 // 60
    current_hour = hours_since - (hours_since // 24) * 24
    minutes_since = since_epoch // 60
    current_minute = minutes_since - (minutes_since // 60) * 60
    second_since = since_epoch // 1
    current_second = second_since - (second_since // 60) * 60
    return current_hour, current_minute, current_second


def days_since_epoch(epoch):
    days = epoch // 60 // 60 // 24
    return days


print(current_time(last_epoch))
print(days_since_epoch(last_epoch))
