import time
from datetime import datetime


def what_time():
    seconds = int(time.time())
    days = seconds // (60 * 60 * 24)
    hours = ((seconds % (60 * 60 * 24)) // 3600) + 2  # + 2 wegens tijdszone en zomeruur
    minutes = ((seconds % (60 * 60 * 24)) % 3600) // 60
    new_seconds = ((seconds % (60 * 60 * 24)) % 3600) % 60

    print(f"The time right now is {hours}:{minutes}:{new_seconds}. {days} days have passed since epoch.")


if __name__ == "__main__":
    what_time()
    print(datetime.now())
