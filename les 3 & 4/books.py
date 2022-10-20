book_price = 24.95
discount = 0.4
copies = 60
standard_shipping = 3
add_shipping = 0.75

price_bookstores = book_price * (1 - discount)
shipping_cost = standard_shipping + (copies - 1) * add_shipping + price_bookstores * copies

print(shipping_cost)
