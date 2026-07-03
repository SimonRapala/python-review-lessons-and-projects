isName = False
while not isName:
  name = input("Enter name: ")

  if name != "":
    isName = True
  else:
    pass
print(f"Hi {name}")

age = -1
while age < 0:
  age = int(input("Enter Your Age: "))

print(f"Your are {age}")