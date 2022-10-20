#pagina 19 - oefening 2 van 2-2
# cover_price book = $24.95,
# bookstores_discount = 40%
# Shipping_costs_for the first copy = $3
# + 0,75 cents for_each_additional copy.
# What is the total wholesale cost for 60 copies?

bookPrice = 24.95
discount = .60
shippingPriceRest = .75
totalUnits = 60
shippingPriceFirst = 3.00
print(((bookPrice * discount) + shippingPriceRest) * totalUnits + shippingPriceFirst)