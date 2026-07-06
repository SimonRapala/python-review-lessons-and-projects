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