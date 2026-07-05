def netPrice(listPrice, salesTax=0.13, discount=0):
  return listPrice * (1 - discount) * (1 + salesTax)

print(netPrice(500, 0.13, 0))
print(netPrice(500))

import time

def count(end, start=0):
  for x in range(start, end+1):
    print(x)
    time.sleep(1)
  print("DONE")

count(10, 5)
count(10)