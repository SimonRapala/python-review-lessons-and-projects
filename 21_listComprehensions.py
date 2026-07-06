doubles = []

for x in range(0, 11):
  doubles.append(x)

for num in doubles:
  doubles[num] = num*2

print(doubles)

doubles.clear()

print(doubles)

doubles = [x * 2 for x in range(0,11)]

print(doubles)

fruits = ["apple", "orange", "banana"]
fruitsUpper = [fruit.upper() for fruit in fruits]
fruitsCap = [fruit.capitalize() for fruit in fruits]

print(fruits)
print(fruitsUpper)
print(fruitsCap)

numbers = [x for x in range(0, 11)]
print(numbers)
evenNum = [x for x in numbers if x % 2 == 0]
oddNum = [x for x in numbers if x % 2 == 1 ]

print(evenNum)
print(oddNum)