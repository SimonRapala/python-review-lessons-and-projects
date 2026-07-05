foods = []
prices = []

while True:
  food = input("What food do you want to buy(q to quit): ")
  if food == "q" or food == "Q":
    break
  else:
    price = float(input(f"Enter the price of {food}: $"))
    foods.append(food)
    prices.append(price)

print("\n----- Cart -----\n")
total = 0
for x in range(len(foods)):
  print(f"{foods[x]} - {prices[x]}")
  total += prices[x]

print(f"Total: ${total}\n")