

def costs(copies):
    cover_price_total = 24.95 * copies * 0.6

    shipping = (3 + (copies - 1) * 0.75)

    return shipping + cover_price_total


print(costs(60))




