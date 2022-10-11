""" Think Python Chapter 5, Exercise 5.1 (p.47)
jvdoorne, @Syntra, 11/10/2022
"""

import time


def time_since_epoch():
    # 1 day = 86400 seconds
    num_days, remainder = divmod(time.time(), 86400)
    # Convert remaining seconds to h, m, s
    mm, ss = divmod(remainder, 60)
    hh, mm = divmod(mm, 60)
    # Output formatted result
    print(f"{hh:02.0f}:{mm:02.0f}:{ss:02.0f} ({int(num_days)} days since epoch)")


if __name__ == '__main__':
    time_since_epoch()
