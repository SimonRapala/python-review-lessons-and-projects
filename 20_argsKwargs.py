def add(*args):
  total = 0
  for arg in args:
    total += arg
  return total

print(add(1, 2, 4, 1, 1, 9))
print(add(1, 2))

def displayName(*args):
  for arg in args:
    print(arg, end=" ")
  print()

displayName("Simon")
displayName("Simon", "Justin", "Kevin", "Vena") 

def printAddr(**kwargs):
  for key, value in kwargs.items():
    print(f"Parameter: {key} - {value}")

printAddr(street="123 Street", city="Oxford", state="Yukon")
printAddr(street="123 Street", city="Oxford", state="Yukon", apt="Microsoft")

def shippingLabel(*args, **kwargs):
  print("To")
  for arg in args:
    print(arg, end=" ")
  print("\nAt")
  for key, value in kwargs.items():
    print(f"{key} - {value}")



shippingLabel("Simon", "Rapala", street="Fake St", city="New York", country="USA")