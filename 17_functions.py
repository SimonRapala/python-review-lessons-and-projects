def birthday(name, age):
  print(f"Happy Birthday {name}!!! You are {age}!!!")

birthday("Simon", 21)
birthday("Steve", 30)
birthday("Beth", 18)

def add(a,b):
  return a + b

print(add(10, 11))

def invoice(user, amount, dueDate):
  print(f"Hello {user}, ${amount} is due on {dueDate}")

invoice("Simon", 3000, "Jan 16")