fruits = ["apple", "banana", "orange"]
meats = ["fish", " chicken", "turkey"]
vegs = ["celery", "carrots", "potatoes"]

groceries = [fruits, vegs, meats]

print(groceries[0][0])
groceries[2].append("boar")
print(groceries)

for collection in groceries:
  for food in collection:
    print(food, end=" ")
  print()

numPad = ((1, 2, 3), (4,5,6),(7,8,9), ("*",0,"#"))

for row in numPad:
  for element in row:
    print(element, end=" ")
  print()