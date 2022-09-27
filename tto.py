price = 24.95
price_discount = price -price/100 * 40
result = round(price_discount * 60 + 3 + (59*0.75),2)
print(result)
