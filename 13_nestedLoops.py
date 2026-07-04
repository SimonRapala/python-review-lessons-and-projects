for i in range(3):
  print("")
  for x in range(1,10):
    print(x, end="")

rows = int(input("\nEnter number of rows: "))
cols = int(input("Enter number of cols: "))
symbol = input("What symbol do you wan to use: ")

for y in range(rows):
  for x in range(cols):
    print(symbol, end="")
  print()