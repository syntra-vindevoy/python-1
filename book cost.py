bookPrice = 24.95
discount = 0.60
shippingPriceRest = 0.75
shippingPriceFirst = 3.00
totalUnits = 60
totalCostBeforeShipping = (bookPrice * discount) * totalUnits
shipping = (shippingPriceRest * (totalUnits-1)) + shippingPriceFirst
result = totalCostBeforeShipping + shipping
print("The total price for 60 books including shipping and discount is: ")
print("Total price of the books is: " + str(totalCostBeforeShipping))
print("Total Shipping is: " + str(shipping))
print("end price is : ", round(result, 2))
print( f"Total cost : {round (result ,2)}")

