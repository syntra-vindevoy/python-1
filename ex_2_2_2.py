amount_bought = 60

price = 24.95
discount = 40 / 100

shipping_cost_first = 3
shipping_cost_next = 0.75

cost_books = amount_bought * price * (1 - discount)
shipping_cost = (amount_bought - 1) * shipping_cost_next + shipping_cost_first

total_cost = cost_books + shipping_cost

print(f"Total cost: {round(total_cost, 2)}")
