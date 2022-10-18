copies = 60
price = 24.95
discount = 0.40
total_cost = price*(1-discount)*copies + 0.75*(copies-1) + 3
print(total_cost)
#dit zou je kunnen opsplitsen in boekenkost en verzendkost, dit is achteraf makkeijker om te debuggen
total_cost = round(total_cost,2) #round(x,y) is functie die x afrondt tot op y decimalen na komma
print(f" The total cost is {total_cost} dollars")


