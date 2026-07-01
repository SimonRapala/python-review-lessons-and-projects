import math
friends = 0
friends += 1#same as friends = friends + 1 works wioth -=, *=, /=
print(friends)

friends *= 3
print(friends)

friends /= 2
print(friends)

friends **= 2
print(friends)

friends %= 3
print(friends)

x = 3.14
y = -4
z = 5

print(round(x))

print(abs(y))

print(pow(y, z))

print(max(x, y, z))

print(min(x, y, z))

print(math.pi)

print(math.e)

print(math.sqrt(64))
print(math.ceil(x))
print(math.floor(x))

rad = float(input("Enter radius of circle: "))
print(f"Circumference : {round(2 * math.pi * rad, 2)}")
print(f"Area : {round(math.pi * pow(rad, 2), 2)}")

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))

print(f"The hypotonuse is : {round(math.sqrt(pow(a, 2) + pow(b, 2)), 2)}")