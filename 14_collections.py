# List = [] ordered and changable. Dupes ok
# Set = {} unordered and immutable, Add or Remove ok. NO DUPES
# Tuple = () ordered and unchangeable. Dupes ok. FASTER

fruits = ["apple", "orange","banana"]

print(fruits[0:2])

for fruit in fruits:
  print(fruit)

print("Hi " + fruits.pop())

print("apple" in fruits)
print("banana" in fruits)

fruits.insert(0, "pineapple")
print(fruits)
fruits.clear()
print(fruits)

fruits = {"apple", "orange","banana"}
fruits.add("pineapple")
print(fruits)
print("pineapple" in fruits)

fruits.clear()

fruits = ("apple", "orange","banana")

print(fruits.index("apple"))