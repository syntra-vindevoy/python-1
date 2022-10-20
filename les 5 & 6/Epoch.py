import time
epoch = time.time()

days = epoch // (60 * 60 * 24)
epoch -= days * 3600 * 24
hours = epoch // 3600
epoch -= hours * 3600
minutes = epoch // 60
seconds = int(epoch % 60)

print(f'{days} days, {hours} hours, {minutes} minutes and {seconds} seconds since epoch')
