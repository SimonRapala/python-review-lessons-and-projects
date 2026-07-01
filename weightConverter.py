weight = float(input("Enter a Weight: "))
unit = input("Enter lbs or  kg: ")

unit = unit.lower()

if not unit or not weight:
  print("Did not enter valid values")
elif unit == "kg":
  print(f"Your weight is {round(weight*2.2, 2)} lbs")
elif unit == "lbs":
  print(f"Your weight is {round(weight/2.2, 2)} kg")
else:
  print("Did not enter valid unit")