# Exercise 2.2. Practice using the Python interpreter as a calculator:
# 1. The volume of a sphere with radius r is 4/3 *  pi * r tot de 3e macht
pi = 3.14159265


# . What is the volume of a sphere with radius 5?

r = 5
volume = 4 / 3 * pi * r**3
print(f"volume of a sphere with radius {r} is {volume}")

# 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
# $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
# 60 copies?
cover_price = 24.95
cover_price_with_discount = 24.95 * 0.6
shipping_costs = 3
shipping_costs_discount = 0.75
amount = 60
total_price = (cover_price_with_discount * 60) + shipping_costs + ((amount - 1) * shipping_costs_discount)
print(f"Total price is {round(total_price, 2)}")

# 3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
# tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
time = (6 * 60 * 60) + (52 * 60)
duration_1_seconds = (8 * 60) + 15
duration_2_seconds = ((7 * 60) + 12) * 3
duration_3_seconds = (8 * 60) + 15
end_time_total_seconds = time + duration_1_seconds + duration_2_seconds + duration_3_seconds
end_time_hour = end_time_total_seconds // 3600
end_time_minutes = (end_time_total_seconds - (end_time_hour * 3600)) // 60
end_time_seconds = (end_time_total_seconds - (end_time_hour * 3600) - (end_time_minutes * 60)) % 60
print(f"home for breakfast at : {end_time_hour}:{end_time_minutes}:{end_time_seconds}")


# 3 idem met datetime
# import datetime
#
# time = datetime.time(6,52,0)
# duration_1_seconds = datetime.time(0,8,15)
# duration_2_seconds = datetime.time(0,7,12)
# duration_3_seconds = datetime.time(0,8,15)
