book_price = 24.95
discount = 0.4
shipping1 = 3
shipping_rest = 0.75
x_books = 60

total_book_cost = (book_price * x_books) - (book_price * x_books * discount)
total_shipping_cost = shipping1 + ((x_books-1) * shipping_rest)
total_cost = total_shipping_cost + total_book_cost

print(f"de prijs is {round(total_cost)}")

