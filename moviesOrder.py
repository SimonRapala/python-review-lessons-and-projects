menu = {
  "pizza": 3.50,
  "coke" : 2.2,
  "hot dog" : 3.00,
  "chips":3.00,
  "popcorn": 6.99
        }
order = []

print("----MENU----")
for item in menu:
  print(f"{item} - ${menu.get(item):.2f}")

while True:
  menuItem = input("What would You like(q to exit): ").lower()
  if menuItem == "q":
    break
  elif menuItem in menu:
    order.append(menuItem)
  else:
    print("Item is not on menu!!!")

total = 0

for item in order:
  total += menu.get(item)
print(f"Order is :{order}. Total is ${total}")