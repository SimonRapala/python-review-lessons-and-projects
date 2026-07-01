age = int(input("What is your age: "))

if age >= 18:
  print("You can get a credit card")
elif age < 0:
  print("Not born yet")
elif age < 5:
  print("Way to young")
else:
  print("You cannot get a credit card")

ans = input("Would you like some food?")

if not ans:
  print("You did not give an ans!")
elif ans == "Yes":
  print("Here is some food!")
else:
  print("No food for you!")